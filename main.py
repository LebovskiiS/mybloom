import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from Exception import Base as ExeBase
from data_base.postgres import engine
from user.router import router as user_router
from farm.router import router as farm_router
from models import Base


app = FastAPI(debug= True)

@app.get('/')
async def test():
    async with engine.begin() as db:
        await db.run_sync(Base.metadata.create_all)


app.include_router(user_router, prefix='/user')
app.include_router(farm_router, prefix='/farm')

@app.exception_handler(ExeBase)
async def base_app_exception_handler(request: Request, ex: ExeBase):
    return JSONResponse(status_code= ex.status_code, content= {"detail": ex.message})




if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=5555)



