from pydantic import BaseModel


class PersonCreate(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_num: str
    group_id: int
