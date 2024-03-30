from datetime import datetime, date
from typing import List
from src.base import Base
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped


class Person(Base):
    __tablename__ = 'person'

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    phone_num: Mapped[str] = mapped_column(nullable=False, unique=True)
    birth_date: Mapped[date] = mapped_column(nullable=False)
    added_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    group_id: Mapped[int | None] = mapped_column(ForeignKey('group.id'))

    group: Mapped['Group'] = relationship(back_populates='person')
    record: Mapped[List['Record']] = relationship(back_populates='person', cascade='save-update, merge, delete',
                                                  passive_deletes=True)

    def __repr__(self) -> str:
        return (f'Person(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r},'
                f'phone_num={self.phone_num!r}), birth_date={self.birth_date!r},'
                f'added_at={self.added_at!r}, group_id={self.group_id!r}')
