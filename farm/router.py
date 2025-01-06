from .schemas import FarmCreate, FarmDelete, FarmUpdate
from fastapi import APIRouter, Depends
from security.authorisation import get_jwt_from_header, get_current_user
from models import UserModel, FarmsModel
from .repository import  add_farm
from sqlalchemy.ext.asyncio import AsyncSession
from data_base.postgres import get_session


router = APIRouter()

@router.post('/create')
async def farm_create(
        farm_data: FarmCreate,
        user: UserModel = Depends(get_current_user),
        session: AsyncSession = Depends(get_session)
):
    new_farm = FarmsModel(
        farm_name=farm_data.name,
        land_size=farm_data.land_size,
        plants_id=farm_data.plants_id
    )
    farm_id = await add_farm(new_farm, user, session)
    return {"success": True, "farm_id": farm_id, 'status': 201, 'message': 'Farm created'}




@router.put('/update')
async def farm_update(userdata: FarmUpdate):
    return userdata



@router.get('')
async def get_farm(farm_id: int):
    return farm_id

