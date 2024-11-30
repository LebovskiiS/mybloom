import asyncio
from models import Base, UserModel
from sqlalchemy.ext.asyncio import create_async_engine
from config import DB_NAME,DB_PORT, DB_HOSTNAME, DB_PASSWORD,DB_USER
from asyncpg import Connection
from typing import Optional
from uuid import uuid4
from sqlalchemy import insert, update, select, delete
import time



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



