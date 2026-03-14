from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.database import get_db
from api.schemas import UserCreate, UserOut
from api import models
from api.security import get_password_hash
from api.auth import get_current_user # Obtiene el usuario authenticado en el sistema

router = APIRouter(
    prefix= "/users",
    tags= ["Usuarios"]
)

@router.post("/register", response_model = UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """ Registrara un nuevo usuario en el sistema"""
    # Tambien comprobara si el usuario ya existe en el sistema

    existing_user = db.query(models.User).filter(models.User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail = "El nombre del usuario ya esta en uso, por favor usa otro!!!")
    
    # Crear el usuario con su contraseña hasheada

    hashed_password = get_password_hash(user_data.password)
    new_user = models.User(username = user_data.username, hashed_password= hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/me", response_model=UserOut)
def get_me(current_user: models.User = Depends(get_current_user)):
    """Devuelve informacion del usuario authenticado"""
    return current_user

@router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    """Lista todo los usuarios registrados, Este endpoint es util para pruebas y depuracion"""

    return db.query(models.User).all()