from pydantic import BaseModel, Field, EmailStr


class ShortUserSchema(BaseModel):
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class UserSchema(ShortUserSchema):
    id: str

class CreateUserRequestSchema(ShortUserSchema):
    """
    Структура данных для создания нового пользователя.
    """
    pass

class CreateUserResponseSchema(BaseModel):
    """
    Структура ответа на запрос создания нового пользователя.
    """
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    """
    Структура ответа на запрос получения информации о пользователе.
    """
    user: CreateUserRequestSchema