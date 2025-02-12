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


async def add_sort(sort: SortModel, session: AsyncSession):
    session.add(sort)
    await session.commit()
    return sort


async def delete_sort(sort: SortModel, session: AsyncSession):
    await session.delete(sort)
    await session.commit()


async def get_sort_by_id(sort_id: int, session: AsyncSession):
    stmt = select(SortModel).where(SortModel.id == sort_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def update_sort(sort: SortModel, session: AsyncSession):
    data = await session.refresh(sort)
    await session.commit()
    return data
