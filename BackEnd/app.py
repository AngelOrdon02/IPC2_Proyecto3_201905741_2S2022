# Importando librerias
from flask import Flask, jsonify, request
from flask_cors import CORS

import json

# Importando modelos
from user import User

app = Flask(__name__)

CORS(app)

# Declaracion de objetos
Users = []

# Datos ingresados
Users.append(User(1,'Angel', '55555-9', '5-55 zona Roja', 'angel@email.com', 'root', 'root', 1))
Users.append(User(2,'Geovanny', '55555-8', '5-56 zona Roja', 'geo@email.com', 'geo', 'geo', 1))
#Users.append(User(2,'Diego', 'Pinto', 'diego', '123', 2))

# --------------- INICIO RUTAS ---------------

@app.route('/', methods=['GET'])
def rutaInicial():
    #global cont_song
    return ("Corriendo API :D, uff: ")

# --------------- User ---------------

# Get users
@app.route('/users', methods=['GET'])
def selectAllUsers():
    global Users
    Data = []

    for user in Users:
        Fact = {
            'id': user.getId(),
            'name': user.getName(),
            'nit': user.getNit(),
            'address': user.getAddress(),
            'email': user.getEmail(),
            'username': user.getUsername(),
            'password': user.getPassword(),
            'user_type': user.getUser_type()
        }
        Data.append(Fact)
    
    answer = jsonify({'users': Data})
    #answer = jsonify(Data)

    return (answer)

# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)