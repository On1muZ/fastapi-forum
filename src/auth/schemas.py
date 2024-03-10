from uuid import UUID

from pydantic import BaseModel, SecretStr, EmailStr


class UserLoginSchema(BaseModel):
    password: SecretStr
    username: str


class UserRegisterSchema(UserLoginSchema):
    email: EmailStr | None = None
    first_name: str | None = None
    last_name: str | None = None


class UserSchema(UserRegisterSchema):
    profile_picture: str | None = None
