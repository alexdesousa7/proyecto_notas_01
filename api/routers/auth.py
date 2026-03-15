from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from api.database import get_db
from api.auth import login_for_access_token

router = APIRouter(
    prefix = "/auth",
    tags = ["Autenticacion"]
)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session= Depends(get_db)):
    """Iniica sesion y devuelve un token JWT"""

    return login_for_access_token(form_data.username, form_data.password, db)
