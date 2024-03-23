from typing import List
from src.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped


class Group(Base):
    __tablename__ = 'group'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True, autoincrement=True)
    lead_id: Mapped[int] = mapped_column(ForeignKey('person.id', use_alter=True), nullable=False)

    person: Mapped[List['Person']] = relationship(back_populates='group')
    report: Mapped[List['Report']] = relationship(back_populates='group', cascade='save-update, merge, delete')

    def __repr__(self) -> str:
        return f'Group(id={self.id!r}, lead_id={self.lead_id!r})'
