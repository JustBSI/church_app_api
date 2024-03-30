from datetime import datetime
from typing import List
from sqlalchemy import DateTime
from src.base import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped


class Group(Base):
    __tablename__ = 'group'

    lead_id: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    person: Mapped[List['Person']] = relationship(back_populates='group')
    report: Mapped[List['Report']] = relationship(back_populates='group', cascade='save-update, merge, delete',
                                                  passive_deletes=True)

    def __repr__(self) -> str:
        return f'Group(id={self.id!r}, lead_id={self.lead_id!r}, created_at={self.created_at!r})'
