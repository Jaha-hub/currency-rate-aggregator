from sqlalchemy import select, insert, update, delete

from app.wallet.models import Wallet


class WalletRepository:
    def __init__(self, session):
        self.session = session

    async def create(
            self,
            user_id:int,
            f_currency: str,
            f_sum: float,
            s_currency: str,
            s_sum: float
    ):
        stmt = insert(Wallet).values(
            user_id=user_id,
            f_currency=f_currency,
            f_sum=f_sum,
            s_currency=s_currency,
            s_sum=s_sum
        ).returning(Wallet)
        result = await self.session.execute(stmt)
        await self.session.flush()
        wallets = result.scalars().first()
        return wallets

    async def update(
            self,
            user_id:int,
            wallet_id: int,
            f_currency: str,
            f_sum: float,
            s_currency: str,
            s_sum: float
    ):
        stmt = update(Wallet).where(Wallet.id == wallet_id,Wallet.user_id == user_id).values(
            f_currency=f_currency,
            f_sum=f_sum,
            s_currency=s_currency,
            s_sum=s_sum
        )
        await self.session.execute(stmt)
        await self.session.flush()

    async def get_by_id(
            self,
            wallet_id: int,
            user_id:int
    ):
        stmt = select(Wallet).where(Wallet.id == wallet_id,Wallet.user_id == user_id)
        result = await self.session.execute(stmt)
        await self.session.flush()
        wallet = result.scalar_one_or_none()
        return wallet

    async def list(
            self
    ):
        stmt = select(Wallet)
        result = await self.session.execute(stmt)
        wallets = result.scalars().all()
        return wallets

    async def delete(
            self,
            wallet_id: int,
            user_id: int
    ):
        stmt = delete(Wallet).where(Wallet.id == wallet_id,Wallet.user_id == user_id)
        await self.session.execute(stmt)
        await self.session.flush()
