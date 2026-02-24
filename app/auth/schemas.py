import re

from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum

from app.auth.validators import validate_password


class UserRoleEnum(Enum):
    user = 'user'
    admin = 'admin'

class UserBase(BaseModel):
    user_id: int = Field(ge=1)
    fullname: str = Field(max_length=512)
    role: UserRoleEnum = UserRoleEnum.user
    username: str = Field(max_length=512)
    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        """
        Функция для валидации имени пользователя

        Проверка на то что имя пользователя начинается с буквы
        Проверка на то что имя пользователя содержит только буквы, цифры и _

        :param value: значение имени пользователя
        :return: валидированное имя пользователя
        """

        if not re.fullmatch(r'^[A-Za-z][A-Za-z0-9_]*$', value):
            raise ValueError("Имя пользователя должно содержать только буквы, цифры и _")

        return value.lower()

class UserRegister(UserBase):
    password: str

    @field_validator("password", mode="before")
    @classmethod
    def validate_password(cls, value):
        """
        Метод валидации пароля
        """

        return validate_password(value)

class UserCreate(UserRegister):
    role : UserRoleEnum

class UserUpdate(UserBase):
    pass

class ChangePasswordSchema(BaseModel):
    """
    Pydantic моделька для изменения пароля

    Attributes:
        old_password: старый пароль
        new_password: новый пароль
    """

    old_password: str
    new_password: str

    @field_validator( "new_password", mode="before")
    @classmethod
    def validate_password(cls, value):
        """
        Метод валидации пароля
        """

        return validate_password(value)


    @model_validator(mode="after")
    def check_password_match(self):
        if self.old_password == self.new_password:
            raise ValueError("Пароли не должны совпадать")
        return self

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"


class RefreshToken(BaseModel):
    refresh_token: str