from fastapi import APIRouter, Depends
from app.api.manager import CurrencyManager
from app.api.dependencies import get_manager

router = APIRouter(prefix="/currency")


@router.get("/rate")
async def get_rate(
        from_currency: str,
        to_currency: str,
        manager: CurrencyManager = Depends(get_manager)
):
    rate = manager.get_rate(from_currency, to_currency)

    return {
        "from": from_currency,
        "to": to_currency,
        "rate": rate
    }


@router.get("/convert")
async def convert(
        amount: float,
        from_currency: str,
        to_currency: str,
        manager: CurrencyManager = Depends(get_manager)
):
    result = manager.convert(amount, from_currency, to_currency)

    return {
        "amount": amount,
        "result": result,
        "from": from_currency,
        "to": to_currency
    }


@router.get("/analytics")
async def analytics(
        manager: CurrencyManager = Depends(get_manager)
):
    wallet = [
        {"currency": "EUR", "amount": 100, "buy_price": 1.05},
        {"currency": "JPY", "amount": 10000, "buy_price": 0.0068},
    ]

    value = manager.portfolio_value(wallet)
    profit = manager.portfolio_profit(wallet)

    return {
        "portfolio_value": value,
        "profit": profit
    }


@router.get("/")
async def get_all_rates():
    manager: CurrencyManager = Depends(get_manager)
    rates = manager.get_all_rates()
    return {
        "rates": rates
    }
