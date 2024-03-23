from pydantic import BaseModel


class GroupCreate(BaseModel):
    id: int
    lead_id: int
