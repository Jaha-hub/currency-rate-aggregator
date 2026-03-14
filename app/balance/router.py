from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from starlette import status

from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.balance.dependencies import get_balance_manager

from app.balance.managers import BalanceManager
from app.balance.schemas import BalanceCreate

router = APIRouter(
    prefix="/balance",
    tags=["balance"],
)


@cbv(router)
class WalletRouter:
    manager: BalanceManager = Depends(get_balance_manager)

    @router.post(
        "/create",
        status_code=status.HTTP_201_CREATED,
    )
    async def create_wallet(self, request: BalanceCreate, user: User = Depends(get_current_user)):
        return await self.manager.create_balances(request=request, user=user)

    @router.get("/")
    async def get_wallet(self, user: User = Depends(get_current_user)):
        return await self.manager.get_all_balances(user.id)
