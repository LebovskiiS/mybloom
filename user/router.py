from user.schemas import UserRegistration, UserLogin, UserChangePassword, UserLoginOutput
from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.responses import JSONResponse
from user.repository import (create_user, select_user_by_auth_data, change_password, select_user_by_email)
from security.hashing import password_hashing
from data_base.postgres import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from logger import logger
from security.token import create_token, decode_token
from security.authorisation import get_jwt_from_header
from wallet.repository import create_wallet
from models import UserModel
from redis_init import get_redis
from security.authorisation import get_current_user
from utils.wrapers import cash
from farm.repository import add_farm
from models import FarmModel

router = APIRouter()

@router.post('/registration')
async def registration_router(userdata: UserRegistration, session: AsyncSession = Depends(get_session)):
    userdata.password = password_hashing(userdata.password)
    user_id = await create_user(userdata.model_dump(), session)
    await create_wallet(user_id, session)
    response = JSONResponse(
        content= {'user_id': user_id},
        headers= {'jwt':create_token(userdata.email)},
        status_code= 201
    )
    farm = FarmModel(
        user_id=user_id,
        farm_name= userdata.name+"'s farm",
    )
    #creating new farm for the user
    await add_farm(farm, session)
    return response




@router.post('/login')
async def login(userdata: UserLogin, session: AsyncSession = Depends(get_session)):
    logger.debug(f'login started with data {userdata.email}')
    user = await select_user_by_auth_data(userdata.email, userdata.password, session)
    if not user:
        raise HTTPException(403, 'Forbidden. Wrong email or password')

    token = create_token(user.email, user.role)

    return JSONResponse(content={'message':'login success','jwt':token}, status_code= 200)


@router.post('/change-password')
async def change_password_router(
        new_password: str,
        session: AsyncSession = Depends(get_session),
        token: str = Depends(get_jwt_from_header)
):
    logger.debug(f'new password has {type(new_password)}, {token}')
    if not token:
        raise HTTPException(403, 'Forbidden not authorised')
    decoded_token = decode_token(token)
    logger.debug('Token decoded')

    user = await select_user_by_email(decoded_token['email'], session)
    if not user:
        raise HTTPException(403, 'Forbidden. Wrong email or password')
    result = await change_password(user.id, password_hashing(new_password), session)
    if not result:
        raise HTTPException(500, 'internal server error')
    return JSONResponse(
        content= 'password changed. Sucsess',
        status_code= 200
    )



@router.get('', status_code=200)
@cash("user:{user.id}")
async def get_user_router(
        user: UserModel = Depends(get_current_user),
        redis=Depends(get_redis)
):
    return UserLoginOutput.model_validate(user).model_dump()


