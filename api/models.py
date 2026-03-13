from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

# Tabla para generar los usuarios

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index= True)
    username = Column(String, unique= True, index= True)
    hashed_password  = Column(String)

    # Relacion: un usuario puede tener una o mas notas

    notes = relationship("Note", back_populates = "owner")

# Tabla relacionada con las notas

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, index= True)
    content = Column(String)
    created_at = Column(DateTime, default= datetime.utcnow)
    expires_at = Column(DateTime, nullable= True)
    completed = Column(Boolean, default= False)

    # relacion con el usuario dueño de la nota

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="notes") 
