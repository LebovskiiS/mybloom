import asyncio

from security.hashing import password_hashing
from data_base.postgres import engine, get_session
from models import UserModel
from sqlalchemy import insert, update, select, delete, and_

async def create_user(info: dict):
    stmt = insert(UserModel).values(
        name=info['name'],
        surname=info['surname'],
        email=info['email'],
        phone=info['phone'],
        password=info['password'],
        address=info['address']
    ).returning(UserModel.id)
    async with engine.begin() as db:
        result = await db.execute(stmt)
        await db.commit()
        print(result.fetchone())



# async def create_user(info: dict):
#     stmt = insert(UserModel).values(
#         name=info['name'],
#         surname=info['surname'],
#         email=info['email'],
#         phone=info['phone'],
#         password=info['password'],
#         address=info['address']
#     ).returning(UserModel.id)
#     session = await get_session()
#     result = await session.execute(stmt)
#     await session.commit()
#     return result.fetchone()




async def select_user(user_id: int):
    stmt = select(UserModel).where(
        UserModel.id == user_id
    )
    async with engine.begin() as db:
        result = await db.execute(stmt)
        print(result.fetchone())
        return result.fetchone()


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


async def update_user_password(user_id: int, old_password: str, new_password: str):
    stmt = (
        update(UserModel).
        where(and_(UserModel.password == old_password, UserModel.id == user_id)).
        values(password=new_password).
        returning(UserModel.email)
    )
    if stmt:
        async with engine.begin(stmt) as db:
            result = await db.execute(stmt)
            db.commit()
            return result.fetchone()
    else:
        return {"message":"wrong password"}, 403



if __name__ == '__main__':
    user_info = {'name': 'stas', 'surname': 'animal', 'email': 'df@gmail.com',
                 'phone':818813445, 'password':'8788787erted',
                 'address':'aifj84dn83id' }
    asyncio.run(create_user(user_info))