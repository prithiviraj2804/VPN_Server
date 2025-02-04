from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    username: str
    password: str


class CreateUserRequest(BaseModel):
    username: str
    password : str
    role: str
