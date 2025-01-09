from .schemas import FarmCreate, FarmDelete, FarmUpdate
from fastapi import APIRouter, Depends
from security.authorisation import get_jwt_from_header, get_current_user
from models import UserModel, FarmsModel
from .repository import  add_farm, farm_update, select_by_farm_id, get_farm
from sqlalchemy.ext.asyncio import AsyncSession
from data_base.postgres import get_session
from exception import UpdateFarmFailed, FarmsNotFound



router = APIRouter()

@router.post('/create')
async def farm_create_router(
        farm_data: FarmCreate,
        user: UserModel = Depends(get_current_user),
        session: AsyncSession = Depends(get_session)
):
    new_farm = FarmsModel(
        farm_name= farm_data.name,
        land_size= farm_data.land_size,
        user_id= user.id
    )
    farm_id = await add_farm(new_farm, session)
    return {"success": True, "farm_id": farm_id, 'status': 201, 'message': 'Farm created'}




@router.put('/update')
async def farm_update_router(
        farm_data: FarmUpdate,
        session: AsyncSession = Depends(get_session),
        user: UserModel = Depends(get_current_user)
    ):

    farm_data_to_update = FarmsModel(
        farm_name= farm_data.name,
        land_size= farm_data.land_size,
        id= farm_data.farm_id
    )

    if not select_by_farm_id(farm_data.farm_id, user.id, session):
        raise UpdateFarmFailed(message= 'farm is not found', status_code= 404)

    farm_id = await farm_update(farm_data_to_update, session)
    return {"farm_id": farm_id,'message': 'Farm updated'}





@router.get("")
async def get_farm_router(
        session: AsyncSession = Depends(get_session),
        user: UserModel = Depends(get_current_user)
) -> dict[str, str]:
    farm_entity = await get_farm(user.id, session)

    if not farm_entity:
        raise FarmsNotFound("No farm found")

    return {
        "id": int(farm_entity.id),
        "farm_name": farm_entity.farm_name,
        "land_size": str(farm_entity.land_size), 
        "user_id": str(farm_entity.user_id)
    }


