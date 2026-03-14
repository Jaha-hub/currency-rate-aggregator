from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_db
from app.balance.managers import BalanceManager


async def get_balance_manager(session: AsyncSession = Depends(get_db)):
    return BalanceManager(session)

async def get_balance_or_404(
        user_id: int,
        manager: BalanceManager = Depends(get_balance_manager),
):
    return await manager.get_all_balances(user_id)