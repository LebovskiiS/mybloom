from user.schemas import UserRegistration, UserLogin, UserChangePassword
from fastapi import APIRouter
from user.repository import create_user

router = APIRouter()


@router.post('/registration')
async def registration(userdata: UserRegistration):
    await create_user(userdata.model_dump())
    return userdata


@router.post('/login')
async def login(userdata: UserLogin):
    return userdata

@router.post('/change-password')
async def change_password(userdata: UserChangePassword):
    return userdata

