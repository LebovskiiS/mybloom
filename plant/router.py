from typing import Union, List, Optional
from sqlalchemy import select
from .schemas import CreatePlantSchema, RequestPlantSchema, PlantResponseSchema
from fastapi import APIRouter, Depends
from security.authorisation import get_jwt_from_header, get_current_user
from models import UserModel, FarmModel
from sqlalchemy.ext.asyncio import AsyncSession
from data_base.postgres import get_session
from exception import UpdateFarmFailed, FarmsNotFound, PlantCreationError
from .repository import create_plant, get_plants
from farm.repository import get_farm
from sort.repository import get_sort_by_id





router = APIRouter()


@router.post('')
async def plant_create_router(
        plant_info: CreatePlantSchema,
        user: UserModel = Depends(get_current_user),
        session: AsyncSession = Depends(get_session)
):
    if not await get_sort_by_id(plant_info.sort_id, session):
        raise PlantCreationError("Sort id is out of range", 403)
    farm = await get_farm(user.id, session)
    result = await create_plant(farm['id'], plant_info, session )
    if not result:
        raise PlantCreationError('PlantCreationError', status_code= 403)
    return result





#the func getting one or all plants for the farm
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound


@router.get("", status_code=200, response_model=PlantResponseSchema | List[PlantResponseSchema])
async def get_plants_router(
        plant_id: Optional[int] = None,
        user=Depends(get_current_user),
        session: AsyncSession = Depends(get_session)
):
    farm = await get_farm(user.id, session)
    result = await get_plants(farm['id'], plant_id, session)
    if not result:
        raise PlantCreationError("Plant creation failed", status_code=403)

    return result



# @router.put('/update')
# async def plant_update_router():
#     pass
#
#
# @router.delete('/delete')
# async def plant_delete_router():
#     pass
#
#
# @router.get("")
# async def get_plant_by_farm_id_router():
#     pass



    