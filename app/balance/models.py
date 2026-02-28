from sqlalchemy import Column, BigInteger, ForeignKey, Numeric

from app.core.models import Base, IntIdMixin, TimeActionMixin


class Balance(Base, IntIdMixin, TimeActionMixin):
    __tablename__ = "balances"
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    currency = Column(BigInteger)
    sum = Column(Numeric(16,2))

