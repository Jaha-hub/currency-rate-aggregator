from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.core.dependencies import get_db
from app.wallet.managers import WalletManager

async def get_wallet_manager(session: AsyncSession = Depends(get_db)):
    return WalletManager(session)

async def get_wallet_or_404(
        wallet_id: int,
        manager: WalletManager = Depends(get_wallet_manager),
        user: User = Depends(get_current_user)
):
    return await manager.get_by_id(wallet_id, user.id)