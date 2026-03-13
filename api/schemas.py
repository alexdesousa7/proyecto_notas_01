from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Esquema para generar el usuario

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

# Esquemas para generar las notas

class NoteBase(BaseModel):
    title: str
    content: str
    expires_at: Optional[datetime] = None

class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int
    created_at: datetime
    completed: bool
    owner_id: int

    class Config:
        orm_mode = True