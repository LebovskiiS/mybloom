
from .schemas import EditWallet
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from models import WalletModel
from sqlalchemy import insert, update, select
from logger import logger
from exception import CreateWalletError



async def create_wallet(user_id: int, session: AsyncSession) -> WalletModel | None:
    try:
        stmt = insert(WalletModel).values(user_id=user_id).returning(WalletModel.id)
        result = await session.execute(stmt)
        await session.commit()

        wallet_id = result.scalar_one_or_none()
        if wallet_id is None:
            logger.error(f'Insertion did not return valid wallet ID for user_id {user_id}')
            raise CreateWalletError(
                'Failed to create wallet, no ID was returned',
                status_code=501)

        logger.debug(f'create wallet finished with wallet ID {wallet_id}')
        return wallet_id
    except SQLAlchemyError as e:
        logger.error(f'Database error during wallet creation: {e}', exc_info=True)
        raise CreateWalletError('Database error occurred while creating wallet', status_code=501)
    except Exception as e:
        logger.error(f'Unexpected error during wallet creation: {e}', exc_info=True)
        raise CreateWalletError('Unexpected error occurred during wallet creation', status_code=501)
    
    

async def select_wallet_by_user_id(user_id: int, session: AsyncSession) -> WalletModel| None:
    stmt = select(WalletModel).where(
        WalletModel.user_id == user_id
    )
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def edit_wallet(add_info: WalletModel, session: AsyncSession) -> WalletModel.id|None:
    try:
        stmt = (update(WalletModel).where(
            WalletModel.user_id == add_info.user_id).values(
            user_id= add_info.user_id,
            card_number= add_info.card_number,
            card_exp_date= add_info.card_exp_date,
            card_cvv= add_info.card_cvv,
            state= add_info.state,
            city= add_info.city,
            apartment= add_info.apartment,
            zip_code= add_info.zip_code)
        ).returning(WalletModel.id)
        result = await session.execute(stmt)
        await session.commit()
        return result.scalar_one_or_none()
    except Exception as e:
        logger.error(f'{e}')
        raise CreateWalletError(
            'Not successful attempt to add data in wallet',
            status_code=501)















