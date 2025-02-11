import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from security.hashing import password_hashing, verefy_password
from data_base.postgres import engine
from models import SortModel
from sqlalchemy import insert, update, select, delete, and_
from logger import logger
from sqlalchemy.exc import IntegrityError
from exception import NotUniqueData


async def get_all_sorts(session: AsyncSession):
    stmt = select(SortModel)
    data = await session.execute(stmt)
    return data.scalars().all()


async def add_sort(session: AsyncSession, sort: SortModel):
    session.add(sort)
    await session.commit()
    return sort

