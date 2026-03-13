from sqlalchemy.orm import Session
from api import models, schemas
from datetime import datetime

class NoteManager:
    """ Clase encargada de gestionar las operaciones relacionadas con las notas."""
    
    """Lo usaremos para mantener la lógica separada de los endpoints."""

    def __init__(self, db: Session):
        self.db = db
    
    def create_note(self, note_data: schemas.NoteCreate, user_id: int):
        """Crea una nueva nota asociada a un usuario"""
        new_note = models.Note(
            title= note_data.title,
            content= note_data.content,
            expires_at= note_data.expires_at,
            owner_id=user_id
        )
        self.db.add(new_note)
        self.db.commit()
        self.db.refresh(new_note)
        return new_note

    def get_notes(self, user_id: int):
        """Devuelve todas las notas creadas por el usuario"""
        return (
            self.db.query(models.Note)
            .filter(models.Note.owner_id == user_id)
            .all()
        )

    def get_note_by_id(self, note_id: int, user_id: int):
        """"Devuelve una nota espefica si pertenece al usuario"""
        return (
            self.db.query(models.Note)
            .filter(models.Note.id == note_id, models.Note.owner_id == user_id)
            .first()
        )

    def update_note(self, note_id: int, note_data: schemas.NoteCreate, user_id: int):
        """""Actualiza una nota existente de los usuarios""""
        note = self.get_note_by_id(note_id, user_id)
        if not note:
            return None
    
        note.title = note_data.title
        note.content = note_data.content
        note.expires_at = note_data.expires_at

        self.db.commit()
        self.db.refresh(note)
        return note

    def mark_completed(self, note_id: int, user_id: int):
        """Marca las notas como completadas"""
        note = self.get_note_by_id(note_id, user_id)
        if not note:
            return None
    
        note.completed = True
        self.db.commit()
        self.db.refresh(note)
        return note

    def delete_note(self, note_id: int, user_id: int):
        """Elimina una nota que pettenece al usuario"""
        note = self.get_note_by_id(note_id, user_id)
        if not note:
            return None
    
        self.db.delete(note)
        self.db.commit()
        return True    