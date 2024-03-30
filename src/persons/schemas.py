from datetime import date, datetime
from pydantic import BaseModel


class PersonCreate(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_num: str
    birth_date: date
    added_at: datetime
    group_id: int | None
