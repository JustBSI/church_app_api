from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.records.models import Record
from src.records.schemas import RecordCreate

router = APIRouter(
    prefix="/record",
    tags=["record"]
)


@router.get("/{record_id}")
async def get_record_by_id(record_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Record).where(Record.id == record_id)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_new_record(new_record: RecordCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Record).values(**new_record.dict())
    await session.execute(stmt)
    await session.commit()
    return {'record was added': new_record.dict()}


@router.delete("/")
async def delete_record_by_id(record_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Record).where(Record.id == record_id)
    await session.execute(stmt)
    await session.commit()
    return {'record was deleted': record_id}


@router.patch("/")
async def update_record_by_id(info: RecordCreate, record_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Record).values(**info.dict()).where(Record.id == record_id)
    await session.execute(stmt)
    await session.commit()
    return {'updated record': info}
