from .schemas import FarmCreate, FarmDelete, FarmUpdate
from fastapi import APIRouter

router = APIRouter()

@router.post('/create')
async def farm_create(userdata: FarmCreate):
    return userdata

@router.delete('/delete')
async def farm_delete(userdata: FarmDelete):
    return userdata



@router.put('/update')
async def farm_update(userdata: FarmUpdate):
    return userdata



@router.get('')
async def get_farm(farm_id: int):
    return farm_id

