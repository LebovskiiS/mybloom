
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from asyncpg import Connection
from typing import AsyncGenerator
from uuid import uuid4
from config import DB_NAME, DB_PORT,DB_USER,DB_HOSTNAME, DB_PASSWORD



class FixedConnection(Connection):
    def _get_unique_id(self, prefix: str) -> str:
        return f'__asyncpg_{prefix}_{uuid4()}__'


engine = create_async_engine(
f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}',
    echo=False,
    future=True,
    connect_args={
        "statement_cache_size": 0,
        "prepared_statement_cache_size": 0,
        "connection_class": FixedConnection,
    }
)


async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session








