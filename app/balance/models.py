from sqlalchemy import Column, BigInteger, ForeignKey, String, Numeric

from app.core.models import Base, IntIdMixin, TimeActionMixin


class Balance(Base, IntIdMixin, TimeActionMixin):
    __tablename__ = "balance"

    user_id = Column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    f_currency = Column(String, nullable=False)
    f_sum = Column(Numeric(20, 2), nullable=False)
    s_currency = Column(String, nullable=False)
    s_sum = Column(Numeric(20, 2), nullable=False)