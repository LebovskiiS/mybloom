from flask import session

from data_base.postgres import engine
from models import PlantModel, UserModel
from sqlalchemy import insert, update, select, delete, and_
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from exception import DataBaseError
from logger import logger


#
# async def plant_create(new_plant: PlantModel, db_session: AsyncSession):