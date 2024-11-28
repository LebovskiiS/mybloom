import uvicorn
from fastapi import FastAPI
from user.router import router as user_router
from farms.router import router as farm_router



from fastapi import APIRouter

app = FastAPI(debug= True)

app.include_router(user_router)


app.include_router(user_router, prefix='/user')
app.include_router(farm_router, prefix='/farm')



if __name__ == '__main__':
    uvicorn.run(app)