import asyncio
from models import Base, UserModel
from sqlalchemy.ext.asyncio import create_async_engine
from config import DB_NAME,DB_PORT, DB_HOSTNAME, DB_PASSWORD,DB_USER
from asyncpg import Connection
from typing import Optional
from uuid import uuid4
from sqlalchemy import insert, update, select, delete



class FixedConnection(Connection):
    def _get_unique_id(self, prefix: str) -> str:
        return f'__asyncpg_{prefix}_{uuid4()}__'

engine = create_async_engine(
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}",
    echo=False,
    future=True,
    connect_args={
        "statement_cache_size": 0,
        "prepared_statement_cache_size": 0,
        "connection_class": FixedConnection,
    }
)


async def create_tables():
    async with engine.begin() as db:
        await db.run_sync(Base.metadata.create_all)


async def create_user(info: dict):
    stmt = insert(UserModel).values(
        name= info['name'],
        surname= info['surname'],
        email= info['email'],
        phone= info['phone'],
        password= info['password'],
        address = info['address']
    ).returning(UserModel.id)
    async with engine.begin() as db:
        result = await db.execute(stmt)
        await db.commit()
        print(result.fetchone())


async def select_user(user_id: int):
    stmt = select(UserModel).where(
         UserModel.id == user_id
    )
    async with engine.begin() as db:
        result = await db.execute(stmt)
        print(result.fetchone())


async def delete_user(user_id: Optional[int]= None):
    if user_id:
        stmt = delete(UserModel).where(UserModel.id == user_id
        )
        async with engine.begin() as db:
            await db.execute(stmt)
            db.commit()
            return 'ok'
    else:
        stmt = delete(UserModel)
        async with engine.begin() as db:
            await db.execute(stmt)
            db.commit()
            return 'ok'


async def update_user_email(user_id: int):
    stmt = update(UserModel).where(UserModel.id == user_id)
    async with engine.begin(stmt) as db:
        await result = db.execute(stmt)
        db.commit()
        return result.lastrowid()







if __name__ == '__main__':
    # asyncio.run(create_user({'name':'stas', 'surname':'animal', 'email':'df@gmail.com',
    #                          'phone':818813445, 'password':'8788787erted', 'address':'aifj84dn83id' }))
    asyncio.run(select_user(7))