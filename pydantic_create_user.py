"""
Pydantic-модели для эндпоинта создания пользователя POST /api/v1/users.
Содержит модели для запроса, ответа и представления данных пользователя.
"""
from pydantic import BaseModel, EmailStr, constr


class UserSchema(BaseModel):
    """
    Схема данных пользователя.
    """
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя.
    """
    mail: EmailStr
    password: constr(min_length=1, max_length=250)
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа на создание пользователя.
    """
    user: UserSchema