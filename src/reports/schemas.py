from datetime import datetime
from pydantic import BaseModel


class ReportCreate(BaseModel):
    id: int
    group_id: int
    created_at: datetime
