import uvicorn
from fastapi import FastAPI
from user.router import router as user_router

app = FastAPI(debug= True)

app.include_router(user_router)

from user.router import router as router_user
app.include_router(router_user, prefix='user')




if __name__ == '__main__':
    uvicorn.run(app)