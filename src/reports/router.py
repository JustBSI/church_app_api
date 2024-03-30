from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.reports.models import Report
from src.reports.schemas import ReportCreate

router = APIRouter(
    prefix="/report",
    tags=["report"]
)


@router.get("/{report_id}")
async def get_report_by_id(report_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Report).where(Report.id == report_id)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_new_report(new_report: ReportCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Report).values(**new_report.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success', 'data': new_report.dict()}


@router.delete("/")
async def delete_report_by_id(report_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Report).where(Report.id == report_id)
    await session.execute(stmt)
    await session.commit()
    return {'report was deleted': report_id}


@router.patch("/")
async def update_report_by_id(info: ReportCreate, report_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Report).values(**info.dict()).where(Report.id == report_id)
    await session.execute(stmt)
    await session.commit()
    return {'updated report': info}
