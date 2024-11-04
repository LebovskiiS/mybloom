import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field



app = FastAPI(debug= True)


class UserRegistration(BaseModel):
    name: str = Field(max_length= 20)
    surname: str = Field(max_length= 20)
    email: str = Field(max_length= 20)
    phone: int
    password: str = Field(max_length= 20)
    address: str = Field(max_length= 20)




@app.post('/registration')
async def registration(userdata: UserRegistration):
    return userdata



@app.post('/')
async def test(something: str|None = None):
    return something






if __name__ == '__main__':
    uvicorn.run(app)