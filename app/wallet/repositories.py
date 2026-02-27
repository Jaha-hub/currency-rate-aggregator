from fastapi.params import Depends
from sqlalchemy.dialects.mysql import insert

from app.wallet.dependencies import get_wallet_or_404
from sqlalchemy import update, select
from app.wallet.models import Wallet

class WalletRepository:
    def __init__(self, session):
        self.session = session

    async def create_wallet(
            self,
            user_id,
    ):
        stmt = insert(Wallet).values(
            user_id=user_id,
        ).returning(Wallet)
        result = await self.session.execute(stmt)
        await self.session.flush()
        wallet = result.scalar_one_or_none()
        return wallet


    async def update_wallet_balance(
            self,
            wallet_id: int,
            user_id: int,
            amount: int,
    ) -> Wallet:
        stmt = (
            update(Wallet)
            .where(
                Wallet.id == wallet_id,
                Wallet.user_id == user_id
            )
            .values(balance=Wallet.f_sum + amount)

            .returning(Wallet)
        )
        result = await self.session.execute(stmt)
        wallet = result.scalar_one_or_none()
        if not wallet:
            raise ValueError("Кошелек не найден")
        await self.session.commit()
        return wallet

    async def get_wallet_by_user_id(
            self,
            user_id: int,
            wallet: Wallet = Depends(get_wallet_or_404),
    ):
        stmt = select(Wallet).where(wallet.user_id == user_id)
        result = await self.session.execute(stmt)
        await self.session.flush()
        wallet = result.scalar_one_or_none()
        return wallet

