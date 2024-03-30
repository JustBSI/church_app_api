from pydantic import BaseModel
from datetime import datetime


class GroupCreate(BaseModel):
    id: int
    lead_id: int
    created_at: datetime
