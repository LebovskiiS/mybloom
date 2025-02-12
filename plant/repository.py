from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CreatePlantSchema, RequestPlantSchema
from models import PlantModel, FarmModel
from sqlalchemy import insert, select
from farm.repository import get_farm
from exception import PlantNotFound
from typing import Optional

async def create_plant(farm_id: int, plant_info: CreatePlantSchema, session: AsyncSession) -> int | None:
    stmt = insert(PlantModel).values(
        farm_id= farm_id,
        name= plant_info.name,
        sort_id= plant_info.sort_id,
        start_time= plant_info.start_time,
        end_time= plant_info.end_time,
        growing_on_percent= plant_info.growing_on_percent,
        is_active= plant_info.is_active
    ).returning(PlantModel.id)

    result = await session.execute(stmt)
    await session.commit()
    return result.scalar_one_or_none()


async def get_plants(farm_id: int, plant_id: Optional[int] , session: AsyncSession):
    if plant_id:
        stmt = select(PlantModel).where(
            PlantModel.id == plant_id,
            PlantModel.farm_id == farm_id
        )
        result = await session.execute(stmt)
        plant = result.scalar_one_or_none()

        if not plant:
            raise PlantNotFound('Plant not found for this farm', status_code=404)
        return plant

    stmt = select(PlantModel).where(PlantModel.farm_id == farm_id)
    result = await session.execute(stmt)
    plants = result.scalars().all()
    return plants

