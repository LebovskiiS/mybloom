from user.schemas import UserRegistration, UserLogin, UserChangePassword
from fastapi import APIRouter
from user.repository import create_user, select_user, delete_user, update_user_password
from security.hashing import password_hashing
router = APIRouter()



@router.post('/registration')
async def registration(userdata: UserRegistration):
    return {"id": await create_user(userdata.model_dump())}



@router.post('/login')
async def login(userdata: UserLogin):
    return userdata


@router.post('/change-password')
async def change_password(old_password: UserChangePassword, new_password: UserChangePassword):
    hashed_old_pass = await password_hashing(old_password.password)
    hashed_new_pass = await password_hashing(new_password)
    return await update_user_password(hashed_old_pass, hashed_new_pass)


@router.get('')
async def get_user_router(id: int):
    return await select_user(id)


@router.delete('')
async def delete_user_router(id:int):
    return await delete_user(id)
