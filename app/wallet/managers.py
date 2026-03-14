from sqlalchemy.ext.asyncio import AsyncSession

from app.wallet.schemas import WalletCreate
from app.wallet.repositories import WalletRepository
from app.wallet.schemas import WalletUpdate


class WalletManager:
    def __init__(
            self,
            session: AsyncSession,
    ):
        self.session = session
        self.wallet_repo = WalletRepository(session)

    async def create(
            self,
            user_id: int,
            request: WalletCreate
    ):
        wallets = await self.wallet_repo.create(
            user_id=user_id,
            f_currency=request.f_currency,
            f_sum=request.f_sum,
            s_currency=request.s_currency,
            s_sum=request.s_sum,
        )
        await self.session.commit()
        return wallets

    async def get_by_id(
            self,
            wallet_id: int,
            user_id: int,
    ):
        wallets = await self.wallet_repo.get_by_id(wallet_id,user_id)
        await self.session.commit()
        return wallets

    async def list(
            self
    ):
        categories = await self.wallet_repo.list()
        return categories

    async def update(
            self,
            wallet_id: int,
            user_id: int,
            request: WalletUpdate
    ):
        await self.wallet_repo.update(
            user_id=user_id,
            wallet_id=wallet_id,
            f_currency=request.f_currency,
            f_sum=request.f_sum,
            s_currency=request.s_currency,
            s_sum=request.s_sum,
        )
        await self.session.commit()

    async def delete(
            self,
            wallet_id: int,
            user_id: int,
    ):
        await self.wallet_repo.delete(
            wallet_id=wallet_id,
            user_id=user_id
        )
        await self.session.commit()
