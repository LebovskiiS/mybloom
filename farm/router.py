from .schemas import FarmCreate, FarmDelete, FarmUpdate, FarmsResponse
from fastapi import APIRouter, Depends
from security.authorisation import get_current_user
from models import UserModel, FarmModel
from .repository import  add_farm, farm_update, select_by_farm_id, get_farm
from sqlalchemy.ext.asyncio import AsyncSession
from data_base.postgres import get_session
from exception import UpdateFarmFailed, FarmsNotFound
from redis_init import get_redis
from utils.wrapers import cash



router = APIRouter()

@router.post('/create')
async def farm_create_router(
        farm_data: FarmCreate,
        user: UserModel = Depends(get_current_user),
        session: AsyncSession = Depends(get_session)
):
    new_farm = FarmModel(
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

    farm_data_to_update = FarmModel(
        farm_name= farm_data.name,
        land_size= farm_data.land_size,
        user_id= user.id
    )

    if not select_by_farm_id(farm_data.farm_id, user.id, session):
        raise UpdateFarmFailed(message= 'farm is not found', status_code= 404)

    farm_id = await farm_update(farm_data_to_update, session)
    return {"farm_id": farm_id,'message': 'Farm updated'}





@router.get("", status_code=200)
@cash("farm_for_user:{user.id}")
async def get_farm_router(
    session: AsyncSession = Depends(get_session),
    user: UserModel = Depends(get_current_user),
    redis=Depends(get_redis),
):
    farm = await get_farm(user.id, session)
    if not farm:
        raise FarmsNotFound("No farm found", 404)
    return farm


