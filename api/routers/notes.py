from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas import NoteCreate, NoteOut
from api.managers.note_manager import NoteManager
# Dependencia que ontendra el usuario authenticado a partir del token JWT
from api.auth import get_current_user


router = APIRouter(
    prefix="/notes",
    tags=["Notas"]
)

@router.get("/", response_model= list[NoteOut])
def list_notes(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    """ Para devolver todas las notas del usuario una vez autenticado"""
    manager = NoteManager(db)
    return manager.get_notes(current_user.id)

@router.post("/", response_model = NoteOut, status_code = status.HTTP_201_CREATED)
def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    """ Crea una nueva nota para el usuario que esta authenticado"""
    manager = NoteManager(db)
    return manager.create_note(note, current_user.id)

@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    """Devuelve una nota determinada si pertenece al usuario"""
    manager = NoteManager(db)
    note = manager.get_note_by_id(note_id, current_user.id)

    if not note:
        raise HTTPException(status_code=404, detail= "La nota no existe!!!")
    
    return note

@router.put("/{note_id}", response_model= NoteOut)
def update_note(note_id: int, note_data: NoteCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    """Actualiza la nota seleccionada, la cual previamente debe de haber sido creada"""
    manager = NoteManager(db)
    update = manager.update_note(note_id, note_data, current_user.id)

    if not update:
        raise HTTPException(status_code=404, detail= "La nota no existe!!!")

    return update

@router.delete("/{note_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    """ Elimina las notas del usuario """
    manager = NoteManager(db)
    delete = manager.delete_note(note_id, current_user.id)

    if not delete:
        raise HTTPException(status_code=404, detail= "La nota no existe!!!")
    
    return None