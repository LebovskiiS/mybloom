from models import FarmModel
from sqlalchemy import insert, update, select
from sqlalchemy.ext.asyncio import AsyncSession
from exception import DataBaseError, UpdateFarmFailed, AddFarmFailed
from logger import logger




async def add_farm(new_farm: FarmModel, db_session: AsyncSession):
    logger.debug(f'add new farm started with data {new_farm}')
    try:
        stmt = insert(FarmModel).values(
            farm_name= new_farm.farm_name,
            land_size= new_farm.land_size,
            user_id= new_farm.user_id
        ).returning(FarmModel.id)

        result = await db_session.execute(stmt)
        await db_session.commit()

        farm_id = result.scalar_one_or_none()
        logger.debug(f'add new farm finished with result {farm_id}')
        return farm_id
    except AddFarmFailed as e:
        logger.error(f'add new farm failed: {e}')
        raise DataBaseError('Not successful attempt to add new farm', status_code= 501)



async def farm_update(farm_model: FarmModel, db_session: AsyncSession):
    logger.debug(f'update farm started with data {farm_model}')
    try:
        stmt = update(FarmModel).where(
            FarmModel.id == farm_model.id).values(
            farm_name = farm_model.farm_name,
            land_size = farm_model.land_size).returning(FarmModel.id
        )

        result = await db_session.execute(stmt)
        await db_session.commit()
        return result.scalar_one_or_none()
    except UpdateFarmFailed as e:
        logger.error(f'update farm failed: {e}')
        raise DataBaseError('Not successful attempt to update farm', status_code= 501)


async def select_by_farm_id(farm_id: int, user_id: int, db_session: AsyncSession) -> FarmModel | None:
    logger.debug('select farm in db started')
    stmt = select(FarmModel).where(
        FarmModel.id == farm_id,
        FarmModel.user_id == user_id
    )
    result = await db_session.execute(stmt)
    logger.debug(f'select farm returned result type: {type(result)}')
    return result.scalar_one_or_none()






async def get_farm(user_id: int, db_session) -> FarmModel | None:
    stmt = select(FarmModel).where(
        FarmModel.user_id == user_id
    )
    result = await db_session.execute(stmt)
    return result.scalar_one_or_none







