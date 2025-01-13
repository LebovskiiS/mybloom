from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from data_base.postgres import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from logger import logger
from wallet.schemas import AddInfoIntoWallet
from models import UserModel, WalletModel
from .repository import add_data_in_wallet
from security.encode_decode_data import encode_data, decode_data
from security.authorisation import get_current_user


router = APIRouter()


@router.post('/edit')
async def wallet_create_router(
        info: AddInfoIntoWallet,
        user: UserModel = Depends(get_current_user),
        session: AsyncSession = Depends(get_session),
) -> JSONResponse:
    logger.debug(f'wallet data added with data {info}')
    wallet = WalletModel(
        user_id=user.id,
        card_number_hash= encode_data(info.card_number),
        card_exp_date= encode_data(info.card_exp_date),
        card_cvv= encode_data(info.card_cvv),
        card_holder= encode_data(info.card_holder),
        state= encode_data(info.state),
        city= encode_data(info.city),
        apartment= encode_data(info.apartment),
        zip_code= encode_data(info.zip_code)
    )
    wallet_id = await add_data_in_wallet(wallet, session)
    logger.debug(f'wallet id {wallet_id}')
    return JSONResponse({'wallet_id': wallet_id, 'message': 'wallet data added'})









