from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.models import User
from app.balance.models import Balance
from app.balance.repositories import BalanceRepository
from app.balance.schemas import BalanceCreate


class BalanceManager:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = BalanceRepository(session)

    async def create_balances(self, user: User, request: BalanceCreate) -> Balance:
        from app.api.manager import CurrencyManager
        curr = CurrencyManager()

        usd = await curr.get_rate(request.f_currency)
        balance_usd = float(request.f_sum) / float(usd)

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
