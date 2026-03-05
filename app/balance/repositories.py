from sqlalchemy.dialects.mysql import insert

from sqlalchemy import update, select
from app.balance.models import Balance


class BalanceRepository:
    def __init__(self, session):
        self.session = session

    async def create_wallet(
            self,
            user_id,
            f_currency,
            f_sum,
            buy_price
    ):
        stmt = insert(Balance).values(
            user_id=user_id,
            f_currency=f_currency,
            f_sum=f_sum,
            buy_price=buy_price
        ).returning(Balance)
        result = await self.session.execute(stmt)
        await self.session.flush()
        wallet = result.scalar_one_or_none()
        return wallet

    async def update_wallet_balance(
            self,
            wallet_id: int,
            user_id: int,
            amount: int,
    ) -> Balance:
        stmt = (update(Balance).where(Balance.id == wallet_id, Balance.user_id == user_id).values(
            Balance.f_sum + amount).returning(Balance))
        result = await self.session.execute(stmt)
        wallet = result.scalar_one_or_none()
        if not wallet:
            raise ValueError("Кошелек не найден")
        await self.session.commit()
        return wallet

    async def get_wallet_by_user_id(
            self,
            user_id: int,
    ):
        stmt = select(Balance).where(Balance.user_id == user_id)
        result = await self.session.execute(stmt)
        await self.session.flush()
        wallet = result.scalar_one_or_none()
        return wallet
