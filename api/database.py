from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Definimos una URL para la base de datos SQLite

DATABASE_URL =  "sqlite:///./notes.db"

# Aqui definimos el motor de la conexion

engine = create_engine (
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Definimos las Sesiones para cada peticion HTTP la cual tendra su propia base de datos

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

# definimos las base para los modelos

Base = declarative_base()

# generamos la dependencia para el FastAPI

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
