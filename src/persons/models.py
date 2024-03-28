from typing import List
from src.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped


class Person(Base):
    __tablename__ = 'person'

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    phone_num: Mapped[str] = mapped_column(nullable=False, unique=True)
    group_id: Mapped[int | None] = mapped_column(ForeignKey('group.id'), default=None, server_default=None)

    group: Mapped['Group'] = relationship(back_populates='person')
    record: Mapped[List['Record']] = relationship(back_populates='person', cascade='save-update, merge, delete')

    def __repr__(self) -> str:
        return (f'Person(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r},'
                f'phone_num={self.phone_num!r}), group_id={self.group_id!r}')
