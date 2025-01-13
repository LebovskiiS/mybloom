import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from exception import Base as ExeBase
from data_base.postgres import engine
from user.router import router as user_router
from farm.router import router as farm_router
from plant.router import router as plant_router
from wallet.router import router as wallet_router
from models import Base
from contextlib import asynccontextmanager
import redis.asyncio as redis
from config import REDIS_PORT


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = redis.Redis(connection_pool=redis.ConnectionPool.from_url(
        f'redis://localhost:{REDIS_PORT}/0', encoding='utf-8', decode_responses=True
    ))
    yield
    await app.state.redis.close()






app = FastAPI(debug= True, lifespan= lifespan)



@app.get('/')
async def test():
    async with engine.begin() as db:
        await db.run_sync(Base.metadata.create_all)



app.include_router(user_router, prefix='/user')
app.include_router(farm_router, prefix='/farm')
app.include_router(plant_router, prefix='/plant')
app.include_router(wallet_router, prefix='/wallet')


@app.exception_handler(ExeBase)
async def base_app_exception_handler(request: Request, ex: ExeBase):
    return JSONResponse(status_code= ex.status_code, content= {"detail": ex.message})




if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=5555)



