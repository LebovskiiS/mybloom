from pydantic import BaseModel, Field



class UserRegistration(BaseModel):
    name: str
    surname: str = Field(max_length=20)
    email: str = Field(min_length=10,max_length=30)
    phone: int
    password: str = Field(min_length=5, max_length=30)
    address: str = Field(max_length=20)



class UserLogin(BaseModel):
    email: str = Field(min_length=10)
    password: str = Field(min_length=5)


class UserChangePassword(BaseModel):
    old_password: str = Field()
    new_password: str = Field(min_length=10)