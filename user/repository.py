import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from security.hashing import password_hashing, verefy_password
from data_base.postgres import engine
from models import UserModel
from sqlalchemy import insert, update, select, delete, and_
from logger import logger
from sqlalchemy.exc import IntegrityError
from exception import NotUniqueData


async def create_user(info: dict, session: AsyncSession):
    logger.debug(f'create user started with data {info}')
    try:
        stmt = insert(UserModel).values(
            name=info['name'],
            surname=info['surname'],
            email=info['email'],
            phone=info['phone'],
            password=info['password'],
            address=info['address']
        ).returning(UserModel.id)
        result = await session.execute(stmt)
        logger.debug(f'create user finished with result {result}')
        await session.commit()
        return result.scalar()
    except IntegrityError:
        raise NotUniqueData('not unique data', 403)




async def change_password(user_id: int, new_password: str, session: AsyncSession):
    logger.debug(f'change password started with data {user_id}')

    stmt = (update(UserModel).where
            (UserModel.id == user_id).values(password = new_password)).returning(UserModel.id)

    result = await session.execute(stmt)
    logger.debug(f'change password finished with result {result}')
    await session.commit()
    return result.scalar_one_or_none()


async def select_user_by_auth_data(email, password, session: AsyncSession):
    logger.debug(f'select user by auth data started with data {email}, {password}')
    stmt = select(UserModel).where(
        UserModel.email == email)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    logger.debug(f'select user by auth data finished with result {user}')
    if user:
        if verefy_password(password, user.password):
            logger.debug(f'select user by auth data finished with result {user}')
            return user
    else:
        return None


async def delete_user(user_id: int):
    stmt = select(UserModel.id).where(
        UserModel.id == user_id)

    async with engine.begin() as db:
        result = await db.execute(stmt)
        if not result.scalar():
            return {"message": "user not found"}
        else:
            stmt = delete(UserModel).where(UserModel.id == user_id)
            await db.execute(stmt)
            db.commit()


async def select_user_by_email(email: str, session: AsyncSession):
    stmt = (
        select(UserModel).
        where(UserModel.email == email)
    )
    result = await session.execute(stmt)
    return result.scalar_one_or_none()











if __name__ == '__main__':
    user_info = {'name': 'stas', 'surname': 'animal', 'email': 'df@gmail.com',
                 'phone':818813445, 'password':'8788787erted',
                 'address':'aifj84dn83id' }
    asyncio.run(create_user(user_info))