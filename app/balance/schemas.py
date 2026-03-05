from pydantic import BaseModel
from enum import Enum


class CurrencyEnum(str, Enum):
    USD = "USD"
    EUR = "EUR"
    JPY = "JPY"
    CNH = "CNH"
    UZS = "UZS"
    RUB = "RUB"
    CAD = "CAD"

class WalletBase(BaseModel):
    f_currency: CurrencyEnum
    f_sum: int


class WalletCreate(WalletBase):
    pass

class WalletBalanceUpdate(WalletBase):
    pass