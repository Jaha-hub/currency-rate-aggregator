from pydantic import BaseModel, Field
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
    f_sum: float = Field(ge=1)
    s_currency: CurrencyEnum
    s_sum: float = Field(ge=1)

class WalletCreate(WalletBase):
    pass

class WalletBalanceUpdate(WalletBase):
    pass