from pydantic import BaseModel


class RecordCreate(BaseModel):
    id: int
    report_id: int
    person_id: int
    sunday_service: bool
    morning_pray: bool
    thursday_pray: bool
    abstinence: bool
    another_service: bool
    call: bool
    meet: bool
    home_service: bool
    mentoring: bool
    reason_for_absence: str | None
