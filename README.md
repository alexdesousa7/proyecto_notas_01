**API de NOTAS con FastAPI**

Este es el ejercicio del modulo de **Programacion Avanzada** cuyo objetivo principal es implementar una API REST completa con autenticacion JWT, gestion de usuarios y operaciones CRUD sobre notas, distribuidas en los routers y gestionadas mediante la clase NoteManager.

El ejercicio incluye Programacion Orientada a Objetos, validaciones, manejoi de fechas y por ultimo un script de pruebas automatizadas utilizando la libreria request.

Para desarrollar el mismo hemos utilizado los siguientes elementos empezando por lo principal que es Python, entre otros como:

- Python 3.12+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Passlib (bcrypt)
- python-jose (JWT)
- SQLite
- Requests (para pruebas)

Basandonos en la **Programacion Orientada a Objetos** en este proyecto hemos aplicado los siguientes principios como:

- **Clases SQLAlchemy** para representar entidades persistentes.
- **Esquemas Pydantic** para validación y transferencia de datos.
- **Clase personalizada `NoteManager`**, que encapsula lógica de negocio:
  - Limpieza de contenido.
  - Validación de fechas límite.
  - Métodos auxiliares para manipular notas.

La API expone 2 grupos principales de **Endpoints** uno para la gestión de usuarios y  autenticación mediante JWT y otro para operaciones sobre la gestion de notas.

A continuacion se explica una breve explicacion de cada uno de ellos:

Autenticación y usuarios
- POST /users/register
Permite registrar un nuevo usuario en la aplicación.

- POST /auth/login
Permite iniciar sesión y devuelve un token JWT necesario para acceder a las rutas protegidas.

Gestión de notas
- POST /notes/
Crea una nueva nota asociada al usuario autenticado.
- GET /notes/
Devuelve todas las notas del usuario.
- GET /notes/{id}
Obtiene una nota concreta a partir de su ID.
- PUT /notes/{id}
Actualiza los datos de una nota existente.
- DELETE /notes/{id}
Elimina una nota por su ID.
- GET /notes/expired
Devuelve las notas cuya fecha límite ya ha vencido.
- PUT /notes/{id}/complete
Marca una nota como completada.

Por ultimo tenemos un script de pruebas automatizado, donde el mismo registra, inicia sesion, crea una nota, lista las mismas, las actualiza, y elimina, por ultimo una prueba de error, para comprobar que el API funciona de forma correcta.

Autor: **Jose Alexander De Sousa**
Modulo 02 Programacion Avanzada