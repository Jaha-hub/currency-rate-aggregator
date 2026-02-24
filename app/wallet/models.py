from sqlalchemy import Column, BigInteger, ForeignKey, String, Integer

from app.core.models import Base, IntIdMixin, TimeActionMixin


class Wallet(Base, IntIdMixin,TimeActionMixin):
    __tablename__ = "wallets"
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    f_currency = Column(String, nullable=False)
    f_sum = Column(Integer, nullable=False)
