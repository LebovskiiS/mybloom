from .schemas import FarmRegistration, FarmLogin, FarmChangePassword
from fastapi import APIRouter

router = APIRouter()

@router.post('/registration')
async def registration(userdata: FarmRegistration):
    return userdata


