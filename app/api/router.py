from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.manager import CurrencyManager
from app.api.dependencies import get_manager
from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.core.dependencies import get_db

router = APIRouter(
    prefix="/currency",
    tags=["currency"]
)


@cbv(router)
class CurrencyRouter:
    manager: CurrencyManager = Depends(get_manager)

    @router.get("/convert")
    async def convert(
            self,
            amount: float,
            to_currency: str,

    ):
        result = await self.manager.convert(amount, to_currency)

        return {
            "amount": amount,
            "result": result,
            "to": to_currency
        }

    @router.get("/analytics")
    async def analytics(
            self,
            user: User = Depends(get_current_user),
            session: AsyncSession = Depends(get_db)
    ):
        return await self.manager.analyze(user.id, session)

    @router.get("/")
    async def get_all_rates(
            self,
    ):
        rates = await self.manager.get_all_rates()
        return {
            "rates": rates
        }
