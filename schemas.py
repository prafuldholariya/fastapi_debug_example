# schemas.py
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str | None = None
    completed: bool = False


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True
