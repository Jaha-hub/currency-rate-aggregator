from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.core.dependencies import get_db
from app.balance.managers import BalanceManager
from app.balance.schemas import  BalanceCreate

router = APIRouter(
    prefix="/balance",
    tags=["balance"],
)


@cbv(router)
class WalletRouter:
    session: AsyncSession = Depends(get_db)

    @router.post(
        "/create",
        status_code=status.HTTP_201_CREATED,
    )
    async def create_wallet(self, request: BalanceCreate, user: User = Depends(get_current_user)):
        manager = BalanceManager(self.session)
        return await manager.create_balances(request=request, user=user)

    @router.get("/{user_id}")
    async def get_wallet(self, user: User = Depends(get_current_user)):
        manager = BalanceManager(self.session)
        return await manager.get_all_balances(user.id)

