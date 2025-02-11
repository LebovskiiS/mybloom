from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CreatePlantSchema
from models import PlantModel
from sqlalchemy import insert

async def create_plant(farm_id: int, plant_info: CreatePlantSchema, session: AsyncSession) -> int | None:
    stmt = insert(PlantModel).values(
        farm_id= farm_id,
        name= plant_info.name,
        sort_id= plant_info.sort_id,
        start_time= plant_info.start_time,
        end_time= plant_info.end_time,
        total_weight= plant_info.total_weight,
        growing_on_percent= plant_info.growing_on_percent,
        is_active= plant_info.is_active
    ).returning(PlantModel.id)

    result = await session.execute(stmt)
    return result.scalar_one_or_none()