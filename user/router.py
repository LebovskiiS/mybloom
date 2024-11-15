from fastapi import APIRouter
from user.schemas import UserRegistration, UserLogin, UserChangePassword

router = APIRouter()



@router.post('/registration')
async def registration(userdata: UserRegistration):
    return userdata


@router.post('/login')
async def login(userdata: UserLogin):
    return userdata

@router.post('/change-password')
async def change_password(userdata: UserChangePassword):
    return userdata

