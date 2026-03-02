from fastapi import FastAPI
from app.auth.routers import router as auth_router
from app.wallet.router import router as wallet_router

app = FastAPI()

app.include_router(auth_router)
auth_router.include_router(wallet_router)
