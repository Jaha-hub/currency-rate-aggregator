from prompt_toolkit.input.win32 import attach_win32_input
from sqlalchemy import update, select
from sqlalchemy.dialects.mysql import insert

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
            user_id,
            f_sum: int,
            wallet: Wallet,
    ):
        stmt = update(Wallet).where(wallet.user_id == user_id, wallet.id == wallet_id).values(
            f_sum=f_sum,
        )
        result = await self.session.execute(stmt)
        await self.session.flush()

    async def get_wallet_by_user_id(
            self,
            user_id: int,
            wallet: Wallet,
    ):
        stmt = select(Wallet).where(wallet.user_id == user_id)
        result = await self.session.execute(stmt)
        await self.session.flush()
        wallet = result.scalar_one_or_none()
        return wallet

