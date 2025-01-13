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
from wallet.schemas import AddInfoIntoWallet
from models import UserModel, WalletModel
from repository import add_data_in_wallet
from se

router = APIRouter()


@router.post('/edit')
async def wallet_create_router(
        info: AddInfoIntoWallet,
        user: UserModel,
        session: AsyncSession = Depends(get_session),
) -> JSONResponse:
    card_number_ = sha256(info.card_number.encode()).hexdigest()

    wallet = WalletModel(
        user_id=user.id,
        card_number_hash=card_number_hash,
        card_exp_date=info.card_exp_date,
        card_cvv=info.card_cvv,
    )

    await add_data_in_wallet(wallet, session)
    return JSONResponse(
        content={'message': 'Data added'},
        status_code=200
    )
