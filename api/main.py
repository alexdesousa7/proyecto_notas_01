from fastapi import FastAPI
from api.routers import users, notes, auth
from api.database import Base, engine

# Generar las tablas de la bbdd

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Notas",
    description="Proyecto del modulo de Programacion Avanzada, API con autenticacion JWT y CRUD de notas",
    version="1.0.0"
)

# Incluimos los routers

app.include_router(users.router)
app.include_router(notes.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Notas - version 1.0.0" }