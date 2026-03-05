from fastapi import FastAPI

from app.api.test import scheduler
from app.auth.routers import router as auth_router
from app.balance.router import router as balance_router
from app.wallet.router import router as wallet_router

app = FastAPI()


@app.on_event("startup")
def start_scheduler():
    scheduler.start()


app.include_router(auth_router)
app.include_router(balance_router)
app.include_router(wallet_router)
