from _datetime import datetime as date_time
from src.base import Base
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.utils import utcnow


class Record(Base):
    __tablename__ = 'record'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True, autoincrement=True)
    report_id: Mapped[int] = mapped_column(ForeignKey('report.id'), nullable=False)
    person_id: Mapped[int] = mapped_column(ForeignKey('person.id'), nullable=False)
    sunday_service: Mapped[bool] = mapped_column(nullable=False)
    morning_pray: Mapped[bool] = mapped_column(nullable=False)
    thursday_pray: Mapped[bool] = mapped_column(nullable=False)
    abstinence: Mapped[bool] = mapped_column(nullable=False)
    another_service: Mapped[bool] = mapped_column(nullable=False)
    call: Mapped[bool] = mapped_column(nullable=False)
    meet: Mapped[bool] = mapped_column(nullable=False)
    home_service: Mapped[bool] = mapped_column(nullable=False)
    mentoring: Mapped[bool] = mapped_column(nullable=False)
    reason_for_absence: Mapped[str] = mapped_column(nullable=True)

    report: Mapped['Report'] = relationship(back_populates='record')
    person: Mapped['Person'] = relationship(back_populates='record')

    def __repr__(self) -> str:
        return (f'Record(id={self.id!r}, report_id={self.report_id!r}, person_id={self.person_id!r},'
                f'sunday_service={self.sunday_service!r}, morning_pray={self.morning_pray!r},'
                f'thursday_pray={self.thursday_pray!r}, abstinence={self.abstinence!r},'
                f'another_service={self.another_service!r}, call={self.call!r}, meet={self.meet!r},'
                f'home_service={self.home_service!r}, mentoring={self.mentoring!r},'
                f'reason_for_absence={self.reason_for_absence!r}')


class Report(Base):
    __tablename__ = 'report'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True, autoincrement=True)
    datetime: Mapped[date_time] = mapped_column(server_default=utcnow(), nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'), nullable=False)

    group: Mapped['Group'] = relationship(back_populates='report')

    def __repr__(self) -> str:
        return f'Report(id={self.id!r}, datetime={self.datetime!r}, group_id={self.group_id!r}'
