from pydantic import BaseModel, Field, EmailStr



class UserRegistration(BaseModel):
    name: str
    surname: str = Field(max_length=20)
    email: EmailStr
    phone: str
    password: str = Field(min_length=5, max_length=30)
    address: str = Field(max_length=20)



class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field()



class UserChangePassword(BaseModel):
    old_password: str = Field()
    new_password: str = Field(min_length=10)



class UserLoginOutput(BaseModel):
    name: str | None
    surname: str | None
    email: EmailStr | None
    phone: str | None
    address: str | None
    class Config:
        from_attributes = True



