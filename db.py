import asyncio
from models import Base
from sqlalchemy.ext.asyncio import create_async_engine
from config import DB_NAME,DB_PORT,DB_HOST,DB_PASS,DB_USER
from asyncpg import Connection
from uuid import uuid4


class FixedConnection(Connection):
    def _get_unique_id(self, prefix: str) -> str:
        return f'__asyncpg_{prefix}_{uuid4()}__'


engine = create_async_engine(
    f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=False,
    future=True,
    connect_args={
        "statement_cache_size":          0,
        "prepared_statement_cache_size": 0,
        "connection_class":              FixedConnection,
        }
    )


async def create_tables():
    async with engine.begin() as db:
        await db.run_sync(Base.metadata.create_all)





if __name__ == '__main__':
    asyncio.run(create_tables())