from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.persons.models import Person
from src.persons.schemas import PersonCreate

router = APIRouter(
    prefix="/person",
    tags=["person"]
)


@router.get("/{person_id}")
async def get_person_by_id(person_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Person).where(Person.id == person_id)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_new_person(new_person: PersonCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Person).values(new_person.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success', 'data': new_person.dict()}


@router.delete("/")
async def delete_person_by_id(person_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Person).where(Person.id == person_id)
    await session.execute(stmt)
    await session.commit()
    return {'person was deleted': person_id}


@router.patch("/")
async def update_person_by_id(info: PersonCreate, person_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Person).values(info.dict()).where(Person.id == person_id)
    await session.execute(stmt)
    await session.commit()
    return {'updated person': info}
