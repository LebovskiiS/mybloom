import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from exception import Base as ExeBase
from data_base.postgres import engine
from user.router import router as user_router
from farm.router import router as farm_router
from plant.router import router as plant_router
from wallet.router import router as wallet_router
from models import Base
from redis.asyncio import Redis
from config import REDIS_URL
from sort.router import router as sort_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = await Redis.from_url(
        REDIS_URL, encoding="utf-8", decode_responses=True
    )
    yield
    await app.state.redis.close()


app = FastAPI(debug=True, lifespan=lifespan)


@app.get("/")
async def test():

    async with engine.begin() as db:
        #добавить список сортов
        await db.run_sync(Base.metadata.create_all)
    return {"message": "Database initialized successfully"}

@app.get("/test")
async def test():
    return {"response":"Hello world"}



app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(farm_router, prefix="/farm", tags=["farm"])
app.include_router(plant_router, prefix="/plant", tags=["plant"])
app.include_router(wallet_router, prefix="/wallet", tags=["wallet"])

app.include_router(sort_router, prefix="/sort", tags=["sort"])


@app.exception_handler(ExeBase)
async def base_app_exception_handler(request: Request, ex: ExeBase):
    return JSONResponse(status_code=ex.status_code, content={"detail": ex.message})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5555)
