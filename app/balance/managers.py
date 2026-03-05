from app.auth.models import User
from app.balance.models import Balance
from app.balance.repositories import BalanceRepository
from app.balance.schemas import WalletCreate


class BalanceManager:
    def __init__(self, session):
        self.session = session
        self.repo = BalanceRepository(session)

    async def create_balances(self, user: User,request: WalletCreate) -> Balance:
        await self.repo.get_wallet_by_user_id(user.id)

        wallet  = await self.repo.create(user.id, **request.model_dump())
        await self.session.commit()
        return wallet




    async def get_all_balances(
            self,
            user_id: int,
    ):
        return await self.repo.get_all_balances(user_id)