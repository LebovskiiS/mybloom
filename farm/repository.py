from data_base.postgres import engine
from models import FarmsModel, UserModel
from sqlalchemy import insert, update, select, delete, and_
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from exception import DataBaseError
from logger import logger




async def add_farm(new_farm: FarmsModel, user: UserModel, session: AsyncSession):
    logger.debug(f'add new farm started with data {new_farm}')
    try:
        stmt = insert(FarmsModel).values(
            farm_name=new_farm.farm_name,
            land_size=new_farm.land_size,
            user_id=user.id
        ).returning(FarmsModel.id)

        result = await session.execute(stmt)
        await session.commit()

        farm_id = result.scalar_one_or_none()
        logger.debug(f'add new farm finished with result {farm_id}')
        return farm_id
    except Exception as e:
        logger.error(f'add new farm failed: {e}')
        raise DataBaseError('Not successful attempt to add new farm', status_code= 501)




async def get_farms(user_id: int):
    stmt = select(FarmsModel).where(
        FarmsModel.user_id == user_id
    )
    async with engine.begin() as db:
        result = await db.execute(stmt)
        return result.fetchall()







