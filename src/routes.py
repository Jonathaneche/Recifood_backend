from flask import Flask, jsonify
from flask_cors import CORS


from src.repositorio import *


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Bienvenido a Recifood"

#Agregar un usuario
@app.route('/add_user', methods=['POST'])
def new_user():
     create_user()
     return "Usuario creado correctamente, JJ"

#Obtener todos los usuarios
@app.route('/users', methods=['GET'])
def getUsers():
     users = get_all_users()
     return users , "Todos los usuarios"

#Obtener el nombre del usuario
@app.route('/get_user_name/<user_id>', methods=['GET'])
def get_name(user_id):
    data = get_user_name(user_id)
    return  data

# #Obtener un usuario
# @app.route('/users/<int:id>', methods=['GET'])
# def getUser(id):
#      user = get__user_by_id(id)
#      return user


## Favoritos: ##

#Agregar a favoritos
@app.route('/add_favorite', methods=['POST'])
def new_fav():
     add_fav()
     return "Meal recipe added successfully"

#Obtener todas los id de las comidas agregadas a favoritos por un usuario
@app.route('/get_all_favs/<user_id>', methods=['GET'])
def get_favs(user_id):
    data = get_all_favs(user_id)
    return jsonify(message="Favorites meals for this user", data=data)

@app.route('/delete_fav_meal/<user_id>/<idMeal>', methods= ['DELETE'])
def delete_fav(user_id, idMeal):
    delete_fav_meal(user_id, idMeal)
    return "Meal deleted correctly"

@app.route('/update_avatar/<user_id>', methods=['PATCH'])
def new_avatar(user_id):
    update_avatar(user_id)
    return "Avatar actualizado"

if __name__ == "__main__":
    app.run(debug=True)