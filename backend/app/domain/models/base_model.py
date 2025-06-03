from pydantic import BaseModel

class BaseModelWithId(BaseModel):
    id: int

    class Config:
        orm_mode = True
