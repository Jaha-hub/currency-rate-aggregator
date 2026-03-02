from pydantic import BaseModel


class WalletBase(BaseModel):
    user_id: int
    f_currency: str = "USD"
    f_sum: int


class WalletCreate(WalletBase):
    f_sum: int = 1

class WalletBalanceUpdate(WalletBase):
    pass