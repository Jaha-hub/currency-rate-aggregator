from sqlalchemy import Column, String, Text, Boolean

from app.core.models import Base, IntIdMixin, TimeActionMixin


class User(Base, IntIdMixin,TimeActionMixin):
    """

    """
    __tablename__ = "users"
    fullname = Column(String(512), nullable=False)
    role = Column(String(20), nullable=False, default="user")
    username = Column(String(320), nullable=False, unique=True)
    hashed_password = Column(Text, nullable=False)