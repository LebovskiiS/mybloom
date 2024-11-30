import asyncio


from data_base.postgres import engine
from models import UserModel
from sqlalchemy import insert, update, select, delete


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




async def select_user(user_id: int):
    stmt = select(UserModel).where(
        UserModel.id == user_id
    )
    async with engine.begin() as db:
        result = await db.execute(stmt)
        print(result.fetchone())


async def delete_user(user_id: int):
    stmt = delete(UserModel).where(UserModel.id == user_id)
    async with engine.begin() as db:
        await db.execute(stmt)
        db.commit()
        return 'ok'


async def update_user_email(user_id: int):
    stmt = update(UserModel).where(UserModel.id == user_id)
    async with engine.begin(stmt) as db:
        result = await db.execute(stmt)
        db.commit()
        return result.lastrowid()



if __name__ == '__main__':
    user_info = {'name': 'stas', 'surname': 'animal', 'email': 'df@gmail.com',
                 'phone':818813445, 'password':'8788787erted',
                 'address':'aifj84dn83id' }
    asyncio.run(create_user(user_info))