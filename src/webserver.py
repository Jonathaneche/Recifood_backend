from flask import Flask
from flask_cors import CORS


from src.repositorio import *


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hola mundo desde Peñascal"

#Agregar un usuario
@app.route('/add_user', methods=['POST'])
def new_user():
     create_user()
     return "Usuario creado correctamente, JJ"

#Obtener todos los usuarios
@app.route('/all_users', methods=['GET'])
def getUsers():
     users = get_all_users()
     return users , "Todos los usuarios"

#Obtener un usuario
@app.route('/users/<int:id>', methods=['GET'])
def getUser(id):
     user = get__user_by_id(id)
     return user



if __name__ == "__main__":
    app.run(debug=True)