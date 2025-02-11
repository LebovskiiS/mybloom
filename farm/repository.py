from typing import Optional

from models import FarmModel
from sqlalchemy import insert, update, select
from sqlalchemy.ext.asyncio import AsyncSession
from exception import DataBaseError, UpdateFarmFailed, AddFarmFailed, FarmCreationError
from logger import logger
from .schemas import FarmsResponse




async def add_farm(new_farm: FarmModel, session: AsyncSession):
    logger.debug(f'add new farm started with data {new_farm}')
    try:
        stmt = insert(FarmModel).values(
            farm_name= new_farm.farm_name,
            user_id= new_farm.user_id,
            land_size = new_farm.land_size,
        ).returning(FarmModel.id)

        result = await session.execute(stmt)
        await session.commit()

        farm_id = result.scalar_one_or_none()
        logger.debug(f'add new farm finished with result {farm_id}')
        return farm_id
    except AddFarmFailed as e:
        logger.error(f'add new farm failed: {e}')
        raise DataBaseError('Not successful attempt to add new farm', status_code= 501)



async def farm_update(farm_model: FarmModel, session: AsyncSession):
    logger.debug(f'update farm started with data {farm_model}')
    try:
        stmt = update(FarmModel).where(
            FarmModel.user_id == farm_model.user_id).values(
            farm_name = farm_model.farm_name,
            land_size = farm_model.land_size).returning(FarmModel.id
        )

        result = await session.execute(stmt)
        await session.commit()
        return result.scalar_one_or_none()
    except UpdateFarmFailed as e:
        logger.error(f'update farm failed: {e}')
        raise DataBaseError('Not successful attempt to update farm', status_code= 501)


async def select_by_farm_id(farm_id: int, user_id: int, session: AsyncSession) -> FarmModel | None:
    logger.debug('select farm in db started')
    stmt = select(FarmModel).where(
        FarmModel.id == farm_id,
        FarmModel.user_id == user_id
    )
    result = await session.execute(stmt)
    logger.debug(f'select farm returned result type: {type(result)}')
    return result.scalar_one_or_none()


async def get_farm(user_id: int, session) -> dict | None:
    stmt = select(FarmModel).where(
        FarmModel.user_id == user_id
    )
    try:
        result = await session.execute(stmt)
        result = result.scalar_one_or_none()
        logger.error(f'get farm returned result: {result}')
        if result is None:
            return None
        unpacked_entity = FarmsResponse.model_validate(result).model_dump()
        return unpacked_entity
    except Exception as e:
        raise FarmCreationError(f"Farm wasn't created: {e}", 403)






