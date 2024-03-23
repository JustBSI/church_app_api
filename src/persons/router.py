from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.persons.models import Person
from src.persons.schemas import PersonCreate

router = APIRouter(
    prefix="/person",
    tags=["person"]
)


@router.get("/")
async def get_specific_person(group_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Person).where(Person.group_id == group_id)
    result = await session.execute(query)
    print(query)
    return result.mappings().all()


@router.post("/")
async def add_specific_person(new_person: PersonCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Person).values(new_person.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success', 'data': new_person.dict()}
