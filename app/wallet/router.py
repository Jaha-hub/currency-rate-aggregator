from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.wallet.schemas import WalletCreate
from app.wallet.managers import WalletManager
from app.wallet.dependencies import get_wallet_manager
from app.wallet.schemas import WalletUpdate

router = APIRouter(
    prefix="/wallet",
    tags=["wallet"]
)


@cbv(router)
class WalletRouter:
    manager: WalletManager = Depends(get_wallet_manager)

    @router.post("/")
    async def create(self, request: WalletCreate, user: User = Depends(get_current_user)):
        response = await self.manager.create(request=request, user_id=user.id)
        return response

    @router.get("/{wallet_id}")
    async def get_by_id(self, wallet_id: int, user: User = Depends(get_current_user)):
        response = await self.manager.get_by_id(wallet_id, user_id=user.id)
        return response

    @router.get("/")
    async def get_all(self):
        response = await self.manager.list()
        return response

    @router.put("/")
    async def update(self, wallet_id: int, request: WalletUpdate, user: User = Depends(get_current_user)):
        response = await self.manager.update(wallet_id=wallet_id, request=request, user_id=user.id)
        return response

    @router.delete("/")
    async def delete(self, wallet_id: int, user: User = Depends(get_current_user)):
        response = await self.manager.delete(wallet_id=wallet_id, user_id=user.id)
        return response
