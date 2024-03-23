from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.groups.models import Group
from src.groups.schemas import GroupCreate

router = APIRouter(
    prefix="/group",
    tags=["group"]
)


@router.get("/{group_id}")
async def get_group_by_id(group_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Group).where(Group.c.id == group_id)
    await session.execute(query)


@router.get("/{lead_id}")
async def get_group_by_lead_id(lead_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Group).where(Group.c.lead_id == lead_id)
    await session.execute(query)


# @router.post("/")
# async def add_group(new_group: Group.__table__, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(Group).values(new_group.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {'status': 'success', 'data': new_group.dict()}
#
#
# @router.delete("/")
# async def delete_group(group_id: int, session: AsyncSession = Depends(get_async_session)):
#     return {'group was deleted': group_id}

#
# @router.patch("/")
# async def update_group(info: Group.__table__, session: AsyncSession = Depends(get_async_session)):
#     return {'updated group': info}

