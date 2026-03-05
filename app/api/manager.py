class CurrencyManager:

    def __init__(self, redis):
        self.redis = redis
        self.key = "currency_rates"

    def get_rate(self, from_currency: str, to_currency: str) -> float:
        pair = f"{from_currency}{to_currency}"

        rate = self.redis.hget(self.key, pair)

        if rate is None:
            raise ValueError("Rate not found")

        return float(rate)

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        rate = self.get_rate(from_currency, to_currency)
        return amount * rate

    def get_all_rates(self):
        return self.redis.hgetall(self.key)

    def save_rates(self, rates: dict):
        self.redis.hset(self.key, mapping=rates)

    def portfolio_value(self, wallet_records):
        total_value = 0

        for record in wallet_records:
            pair = f"USD{record['currency']}"

            rate = self.get_rate(pair)

            value = record["amount"] * rate
            total_value += value

        return total_value

    def portfolio_profit(self, wallet_records):
        total_profit = 0

        for record in wallet_records:
            pair = f"USD{record['currency']}"
            rate = self.get_rate(pair)

            current_value = record["amount"] * rate
            buy_value = record["amount"] * record["buy_price"]

            profit = current_value - buy_value

            total_profit += profit

        return total_profit
