from datetime import datetime as date_time
from pydantic import BaseModel


class ReportCreate(BaseModel):
    id: int
    datetime: date_time
    group_id: int
