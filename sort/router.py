

from .schemas import ResponseSortSchema, RequestSortSchema, RequestUpdateSort
from fastapi import APIRouter, Depends
from security.authorisation import get_current_user
from models import SortModel, UserModel
from sqlalchemy.ext.asyncio import AsyncSession
from data_base.postgres import get_session
from exception import NoAdminRightsError, DataNotFoundError
from .repository import get_all_sorts, add_sort, delete_sort, get_sort_by_id, update_sort




router = APIRouter()

@router.get('')
async def get_all_sorts_router(
        session: AsyncSession = Depends(get_session), user: UserModel = Depends(get_current_user)
):
    return await get_all_sorts(session)


@router.post('')
async def add_sort_router(
        body: RequestSortSchema,
        session: AsyncSession = Depends(get_session),
        user: UserModel = Depends(get_current_user)):
    if not user.role == 'admin':
        raise NoAdminRightsError( 'Forbidden. No admin rights', 403)
    print(body.grow_time, type(body.grow_time))
    sort = SortModel(
        name= body.name,
        description= body.description,
        color= body.color,
        price= body.price,
        grow_time= body.grow_time,
        unit_weight= body.unit_weight,
        min_unit_number= body.min_unit_number,
    )
    return await add_sort(sort, session)


@router.delete('', status_code=204)
async def remove_sort_router(
        id: int,
        session: AsyncSession = Depends(get_session),
        user: UserModel = Depends(get_current_user)):
    if not user.role == 'admin':
        return NoAdminRightsError( 'Forbidden. No admin rights', 403)
    sort =  await get_sort_by_id(id, session)
    if not sort:
        raise DataNotFoundError( 'Sort not found', 404)
    await delete_sort(sort, session)


@router.put('')
async def update_sort_router(updated_data: RequestUpdateSort,
        session: AsyncSession = Depends(get_session),
        user: UserModel = Depends(get_current_user)):
    if not user.role == 'admin':
        raise NoAdminRightsError( 'Forbidden. No admin rights', 403)
    sort = await get_sort_by_id(updated_data.id, session)
    if not sort:
        raise DataNotFoundError( 'Sort not found', 404)
    sort.name = updated_data.name
    sort.description = updated_data.description
    sort.color = updated_data.color
    sort.price = updated_data.price
    sort.grow_time = updated_data.grow_time
    sort.unit_weight = updated_data.unit_weight
    sort.min_unit_number = updated_data.min_unit_number
    await session.commit()
    await update_sort(sort, session)









