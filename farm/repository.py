from data_base.postgres import engine
from models import FarmsModel
from sqlalchemy import insert, update, select, delete, and_



async def get_farms(user_id: int):
    stmt = select(FarmsModel).where(
        FarmsModel.user_id == user_id
    )
    async with engine.begin() as db:
        result = await db.execute(stmt)
        return result.fetchall()







