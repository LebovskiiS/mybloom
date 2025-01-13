
from schemas import add_infoIntoWallet
from sqlalchemy.ext.asyncio import AsyncSession
from security.hashing import password_hashing, verefy_password
from data_base.postgres import engine
from models import UserModel, WalletModel
from sqlalchemy import insert, update, select, delete, and_
from logger import logger
from sqlalchemy.exc import IntegrityError
from exception import CreateWalletError



async def create_wallet(user_id: int, db_session: AsyncSession) -> WalletModel| None:
    try:
        stmt = insert(WalletModel).values(user_id=user_id).returning(WalletModel.id)
        result = await db_session.execute(stmt)
        await db_session.commit()
        return result.scalar_one_or_none()
    except: 
        raise CreateWalletError(
            'Not successful attempt to create wallet',
            status_code=501)
    
    

async def select_wallet_by_user_id(user_id: int, db_session: AsyncSession) -> WalletModel| None:
    stmt = select(WalletModel).where(
        WalletModel.user_id == user_id
    )
    result = await db_session.execute(stmt)
    return result.scalar_one_or_none()


async def add_data_in_wallet(user_id: int, add_info: add_infoIntoWallet, db_session: AsyncSession) -> WalletModel.id|None:
    try:
        stmt = (update(WalletModel).where(
            WalletModel.user_id == user_id).values(
            card_number= add_info.card_number,
            card_exp_date= add_info.card_exp_date,
            card_cvv= add_info.card_cvv,
            state= add_info.state,
            city= add_info.city,
            apartment= add_info.apartment,
            zip_code= add_info.zip_code)
        ).returning(WalletModel.id)
        result = await db_session.execute(stmt)
        await db_session.commit()
        return result.scalar_one_or_none()
    except:
        raise CreateWalletError(
            'Not successful attempt to add data in wallet',
            status_code=501)















