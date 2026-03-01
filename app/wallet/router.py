from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.core.dependencies import get_db
from app.wallet.managers import WalletManager
from app.wallet.schemas import WalletBalanceUpdate
from app.wallet.models import Wallet
router = APIRouter(
    prefix="/wallet",
    tags=["wallet"],
)
@cbv(router)
class WalletRouter:

    session: AsyncSession = Depends(get_db)
    current_user: User = Depends(get_current_user)

    @router.post(
        "/create",
        status_code=status.HTTP_201_CREATED,
    )
    async def create_wallet(self):
        manager = WalletManager(self.session)

        try:
            wallet = await manager.create_wallet(
                user=self.current_user,
                wallet=Wallet()
            )
            return wallet

        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
            )

    @router.patch(
        "/{wallet_id}/balance",
    )
    async def update_wallet_balance(
        self,
        wallet_id: int,
        data: WalletBalanceUpdate,
    ):
        manager = WalletManager(self.session)

        try:
            wallet = await manager.update_wallet_balance(
                wallet_id=wallet_id,
                user_id=self.current_user.id,
                amount=data.amount,
            )
            return wallet

        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
            )
