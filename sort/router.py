

from .schemas import ResponseSortSchema, RequestSortSchema
from fastapi import APIRouter, Depends
from security.authorisation import get_current_user
from models import SortModel, UserModel
from sqlalchemy.ext.asyncio import AsyncSession
from data_base.postgres import get_session
from exception import NoAdminRightsError
from .repository import get_all_sorts, add_sort




router = APIRouter()

@router.get('')
async def get_all_farms(
        session: AsyncSession = Depends(get_session), user: UserModel = Depends(get_current_user)
):
    return await get_all_sorts(session)


@router.post('/')
async def add_sort_router(
        body: RequestSortSchema,
        session: AsyncSession = Depends(get_session),
        user: UserModel = Depends(get_current_user)):
    if not user.role == 'admin':
        raise NoAdminRightsError( 'Forbidden. No admin rights', 403)
    sort = SortModel(
        name= body.name,
        description= body.description,
        color= body.color,
        price= body.price,
        grow_time= body.grow_time,
        min_unit_number= body.min_unit_number,
    )
    return await add_sort(session, sort)




