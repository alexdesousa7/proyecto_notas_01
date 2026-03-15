import requests

BASE_URL = "http://127.0.0.1:8000"

def register_user(username, password):
    print("*** 1er Prueba: Registrando usuario ***")
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/users/register", json=data)
    print("Status:", response.status_code)
    print("Respuesta:", response.json())
    return response

def login(username, password):
    print("*** 2da Prueba: Iniciando sesión con el usuario***")
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/auth/login", data=data)
    print("Status:", response.status_code)
    print("Respuesta:", response.json())
    return response.json().get("access_token")

def create_note(token, title, content):
    print("*** 3era Prueba: Creando una nota del usuario ***")
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": title, "content": content, "expires_at": None}
    response = requests.post(f"{BASE_URL}/notes/", json=data, headers=headers)
    print("Status:", response.status_code)
    print("Respuesta:", response.json())
    return response.json()

def list_notes(token):
    print("*** 4ta Prueba: Listando las notas del usuario ***")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/notes/", headers=headers)
    print("Status:", response.status_code)
    print("Respuesta:", response.json())
    return response.json()

def update_note(token, note_id, title, content):
    print("*** 5ta Prueba: Actualizando las notas del usuario ***")
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": title, "content": content, "expires_at": None}
    response = requests.put(f"{BASE_URL}/notes/{note_id}", json=data, headers=headers)
    print("Status:", response.status_code)
    print("Respuesta:", response.json())
    return response.json()

def delete_note(token, note_id):
    print("*** 6ta Prueba: Eliminando las notas del usuario ***")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/notes/{note_id}", headers=headers)
    print("Status:", response.status_code)
    print("Respuesta:", response.text)

if __name__ == "__main__":
    # 1. Registrar usuario
    # register_user("alexdesousa", "D1n054uR1o") # Usuario usado en pruebas
    # register_user("alexdesousa02", "D1n054uR1o") # Usuario usado en pruebas
    register_user("alexdesousa03", "D1n054uR1o")

    # 2. Login
    # register_user("alexdesousa", "D1n054uR1o") # Usuario usado en pruebas
    # register_user("alexdesousa02", "D1n054uR1o") # Usuario usado en pruebas    
    token = login("alexdesousa03", "D1n054uR1o")

    # 3. Crear nota
    note = create_note(token, "Mi primera nota de Prueba", "Contenido de la prueba")

    # 4. Listar notas
    notes = list_notes(token)

    # 5. Actualizar nota
    update_note(token, note["id"], "Actualizamos la nota", "Nueva informacion en las notas")

    # 6. Eliminar nota
    delete_note(token, note["id"])