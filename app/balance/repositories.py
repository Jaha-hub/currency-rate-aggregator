from sqlalchemy.dialects.mysql import insert

from sqlalchemy import update, select
from app.balance.models import Balance


class BalanceRepository:
    def __init__(self, session):
        self.session = session

    async def create(
            self,
            user_id:int,
            f_currency: str,
            f_sum: float,
            balance_usd: float,
    ):
        stmt = insert(Balance).values(
            user_id=user_id,
            f_currency=f_currency,
            f_sum=f_sum,
            balance_usd=balance_usd,

        ).returning(Balance)
        result = await self.session.execute(stmt)
        await self.session.flush()
        wallet = result.scalar_one_or_none()
        return wallet

    async def get_by_id(
            self,
            user_id: int,
            balance_id: int
    ):
        stmt = select(Balance).where(Balance.user_id == user_id, Balance.id == balance_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()


    async def get_all_balances(
            self,
            user_id: int,
    ):
        stmt = select(Balance).where(Balance.user_id == user_id)
        result = await self.session.execute(stmt)
        await self.session.flush()
        balances = result.scalars().all()
        return balances