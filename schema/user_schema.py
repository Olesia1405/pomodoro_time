from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    user_id: int
    access_token: str

    class Config:
        from_attributes = True


class UserCreateSchema(BaseModel):
    user_name: str
    password: str

    class Config:
        from_attributes = True