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

# --------------- Auth ---------------

@app.route('/login', methods=['POST'])
def loginUser():
    global Users

    '''
    Si el state = 0 significa que hubo un error
    codigo cero (0) error
    Si el state = 1 significa que si se loggeo con exito
    codigo uno (1) username y password correctos
    Si el state = 2 significa que el password esta incorrecta
    codigo dos (2) username correcto y password incorrecto
    Si el state = 3 significa que el usuario esta incorrecto
    codigo tres (3) username incorrecto y password correcto
    Si el state = 4 significa que los datos son incorrectos
    codigo cuatro (4) username y password incorrectos
    '''

    username = request.json['username']
    password = request.json['password']
    id_user = 0

    state_username = False
    state_password = False
    state = 0

    for i in range(len(Users)):
        if username == Users[i].getUsername():
            state_username = True
            id_user = Users[i].getId()
            break
    
    for i in range(len(Users)):
        if password == Users[i].getPassword():
            state_password = True
            break
    
    if (state_username == False) and (state_password == False):
        state = 4
    elif (state_username == False) and (state_password == True):
        state = 3
    elif (state_username == True) and (state_password == False):
        state = 2
    elif (state_username == True) and (state_password == True):
        state = 1

    answer = jsonify({'message': 'Login process', 'state': state, 'id': id_user})
    return (answer)
    #answer = jsonify({'message': 'Added user'})
    #return (answer)

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

# --------------- Configuraciones ---------------

# msg_config
@app.route('/msg_config', methods=['POST'])
def msg_config():
    
    # Codigo
    # data = request.json()
    data_answer = request.json['data']
    
    answer = jsonify({'message': data_answer})
    return (answer)

# msg_consumption
@app.route('/msg_consumption', methods=['POST'])
def msg_consumption():

    data_answer = request.json['data']

    answer = jsonify({'message': data_answer})
    return (answer)

# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)