from fastapi import FastAPI

from app.api.test import scheduler, update_rates
from app.auth.routers import router as auth_router
from app.balance.router import router as balance_router
from app.wallet.router import router as wallet_router
from app.api.router import router as api_router

app = FastAPI()


@app.on_event("startup")
def start_scheduler():
    # первый запуск сразу
    update_rates()
    # потом стартуем scheduler
    if not scheduler.running:
        scheduler.start()


app.include_router(auth_router)
app.include_router(balance_router)
app.include_router(wallet_router)
app.include_router(api_router)
