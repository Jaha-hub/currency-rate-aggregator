from fastapi import HTTPException
from app.balance.managers import BalanceManager



class CurrencyManager:
    def __init__(self, redis):
        self.redis = redis
        self.key = "currency_rates"
        self.balance = BalanceManager()

    def get_rate(self, from_currency: str, to_currency: str) -> float:
        pair = f"{from_currency}{to_currency}"
        rate = self.redis.hget(self.key, pair)
        if rate is None:
            raise HTTPException(status_code=404, detail=f"Rate for {pair} not found")
        return float(rate)

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        rate = self.get_rate(from_currency, to_currency)
        return amount * rate

    def get_all_rates(self) -> dict:
        return self.redis.hgetall(self.key)

    def analyze(
            self,
            user_id: int,
    ):
        pass


