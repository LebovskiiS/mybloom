from .schemas import CreatePlantSchema
from fastapi import APIRouter, Depends
from security.authorisation import get_jwt_from_header, get_current_user
from models import UserModel, PlantModel
from sqlalchemy.ext.asyncio import AsyncSession
from data_base.postgres import get_session
from exception import UpdateFarmFailed, FarmsNotFound



router = APIRouter()


@router.post('/create')
async def plant_create_router(
        new_plant: CreatePlantSchema,
        user: UserModel = Depends(get_current_user),
        session: AsyncSession = Depends(get_session)
):
    new_plant = PlantModel(

    )

    