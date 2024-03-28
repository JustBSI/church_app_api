from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
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
    query = select(Group).where(Group.id == group_id)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_new_group(new_group: GroupCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Group).values(new_group.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success', 'data': new_group.dict()}


@router.delete("/")
async def delete_group_by_id(group_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Group).where(Group.id == group_id)
    await session.execute(stmt)
    await session.commit()
    return {'group was deleted': group_id}


@router.patch("/")
async def update_group_by_id(info: GroupCreate, group_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Group).values(info.dict()).where(Group.id == group_id)
    await session.execute(stmt)
    await session.commit()
    return {'updated group': info}
