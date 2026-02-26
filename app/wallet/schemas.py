from pydantic import BaseModel, Field


class WalletBase(BaseModel):
    user_id: int
    f_currency: str
    f_sum: int

class WalletCreate(WalletBase):
    pass

class WalletBalanceUpdate(WalletBase):
    pass