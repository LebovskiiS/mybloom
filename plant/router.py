from .schemas import CreatePlantSchema
from fastapi import APIRouter, Depends
from security.authorisation import get_jwt_from_header, get_current_user
from models import UserModel, PlantModel
from sqlalchemy.ext.asyncio import AsyncSession
from data_base.postgres import get_session
from exception import UpdateFarmFailed, FarmsNotFound, PlantCreationError
from .repository import create_plant
from farm.repository import get_farm




router = APIRouter()


@router.post('/create')
async def plant_create_router(
        plant_info: CreatePlantSchema,
        user: UserModel = Depends(get_current_user),
        session: AsyncSession = Depends(get_session)
):
    farm = await get_farm(user.id, session)
    result = await create_plant(farm['id'], plant_info, session )
    if not result:
        raise PlantCreationError('PlantCreationError', status_code= 403)
    return result




# @router.get("", status_code=200)
#
# async def get_farms_router():
#     pass
#
#
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



    