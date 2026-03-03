from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_db
from app.wallet.managers import WalletManager
from app.wallet.models import Wallet


async def get_wallet_manager(session: AsyncSession = Depends(get_db)):
    return WalletManager(session)

async def get_wallet_or_404(
        user_id: int,
        manager: WalletManager = Depends(get_wallet_manager),
):
    return await manager.get_wallet(user_id, Wallet)