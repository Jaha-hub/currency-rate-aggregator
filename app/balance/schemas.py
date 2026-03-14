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

class BalanceBase(BaseModel):
    f_currency: CurrencyEnum
    f_sum: float = Field(ge=1)

class BalanceCreate(BalanceBase):
    pass

class BalanceUpdate(BalanceBase):
    pass

class BalanceRead(BaseModel):
    id: int