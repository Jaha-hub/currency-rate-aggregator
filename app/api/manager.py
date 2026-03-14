from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.client_get import redis_client

from app.balance.managers import BalanceManager


class CurrencyManager:
    def __init__(self):
        self.redis = redis_client
        self.key = "currency_rates"

    async def get_rate(self, to_currency) -> float:

        if hasattr(to_currency, "value"):
            to_currency = to_currency.value

        to_currency = to_currency.upper()

        if to_currency == "USD":
            return 1.0

        pair = f"USD{to_currency}"

        rate = self.redis.hget(self.key, pair)

        if rate is None:
            raise HTTPException(
                status_code=404,
                detail=f"Rate for {pair} not found"
            )

        return float(rate)

    async def convert(self, amount: float, to_currency: str) -> float:
        rate = await self.get_rate(to_currency)
        return amount * rate

    async def get_all_rates(self) -> dict:
        return self.redis.hgetall(self.key)

    async def analyze(
            self,
            user_id: int,
            session: AsyncSession
    ):

        balance_manager = BalanceManager(session)
        balances = await balance_manager.get_all_balances(user_id)

        totals_by_currency = {}
        total_usd_current = 0.0
        balances_original_in_usd = 0

        for b in balances:

            currency = b.f_currency
            balances_original_in_usd += b.balance_usd

            if currency not in totals_by_currency:
                totals_by_currency[currency] = 0

            totals_by_currency[currency] += float(b.f_sum)

            rate = await self.get_rate(currency)

            if currency == "USD":
                total_usd_current += float(b.f_sum)
            else:
                total_usd_current += float(b.f_sum) / rate

        return {
            "user_id": user_id,
            "balances_original": totals_by_currency,
            "balances_original_in_usd": balances_original_in_usd,
            "total_current_usd": round(total_usd_current, 2)
        }
