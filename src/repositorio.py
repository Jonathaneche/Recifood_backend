from flask import request, jsonify
import sqlite3

# Configuración de la base de datos
DB_NAME = 'recifood.db'


# Conexión a la base de datos
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Crear tabla usuarios si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,
                user_id TEXT NOT NULL)''')

# Guardar los cambios y cerrar la conexión
conn.commit()

# Crear tabla favoritos si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS favoritos
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                idMeal INTEGER NOT NULL,
                user_id TEXT NOT NULL)''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()


def get_db_connection():
    # Establece una conexión a la base de datos SQLite
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# Función para crear un nuevo usuario
def create_user():
    # Obtener los datos del usuario desde el JSON de la solicitud
    data = request.json
    nombre = data['nombre']
    correo = data['correo']
    user_id = data['user_id']

    # Conexión a la base de datos
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Insertar el nuevo usuario en la tabla "usuarios"
    cursor.execute('INSERT INTO usuarios (nombre, correo, user_id) VALUES ( ?, ?, ?)',
                   (nombre, correo, user_id))
    conn.commit()

    # Obtener el ID del nuevo usuario insertado
    new_user_id = cursor.lastrowid

    # Cerrar la conexión a la base de datos
    conn.close()

    # Crear el objeto del nuevo usuario con su ID y los demás datos
    new_user = {'id': new_user_id, 'nombre': nombre, 'correo': correo, 'user_id': user_id}

    # Devolver la respuesta en formato JSON con el nuevo usuario creado y el código de estado 201 (Created)
    return jsonify(new_user), 201

# def get_all_users():
#     # Obtiene todas las tareas de la base de datos 
#     # y las devuelve en formato JSON
#     conn = get_db_connection()
#     tasks = conn.execute('SELECT * FROM usuarios').fetchall()
#     conn.close()
#     users_list = [dict(task) for task in tasks]
#     return jsonify(users_list)

def get_all_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM usuarios')
    datos_usuarios = cur.fetchall()
    data = [{'id': dato[0], 'nombre': dato[1], 'correo': dato[2], 'user_id': dato[3]} for dato in datos_usuarios]
    conn.close()
    return jsonify(data)

def get__user_by_id(id):
    # Obtiene una tarea específica según el ID proporcionado
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM usuarios WHERE id = ?', (id,)).fetchone()
    conn.close()
    if user:
        return jsonify(dict(user))
    return jsonify({'error': 'User not found'}), 404




