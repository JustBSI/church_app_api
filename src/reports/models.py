from datetime import datetime as date_time
from src.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.types import DateTime
from typing import List


class Report(Base):
    __tablename__ = 'report'

    datetime: Mapped[date_time] = mapped_column(DateTime(timezone=True), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'), nullable=False)

    group: Mapped['Group'] = relationship(back_populates='report')
    record: Mapped[List['Record']] = relationship(back_populates='report')

    def __repr__(self) -> str:
        return f'Report(id={self.id!r}, datetime={self.datetime!r}, group_id={self.group_id!r}'
