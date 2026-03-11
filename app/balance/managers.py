from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_manager

from app.auth.models import User
from app.balance.models import Balance
from app.balance.repositories import BalanceRepository
from app.balance.schemas import BalanceCreate
from app.core.dependencies import get_db


class BalanceManager:
    def __init__(self, session: AsyncSession = Depends(get_db())):
        self.session = session
        self.repo = BalanceRepository(session)
        self.curr = get_manager()

    async def create_balances(self, user: User, request: BalanceCreate) -> Balance:
        usd = self.curr.get_rate(request.f_currency, "USD")
        balance_usd = int(request.f_sum) * int(usd)

        wallet = await self.repo.create(
            user_id=user.id,
            f_currency=request.f_currency,
            f_sum=request.f_sum,
            balance_usd=balance_usd,
        )
        await self.session.commit()
        return wallet

    async def get_all_balances(
            self,
            user_id: int,
    ):
        return await self.repo.get_all_balances(user_id)
