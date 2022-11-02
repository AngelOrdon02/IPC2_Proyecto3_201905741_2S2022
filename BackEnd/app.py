# Importando librerias
from flask import Flask, jsonify, request
from flask_cors import CORS

import json

# Importando modelos
from user import User
from resource import Resource
from category import Category
from setting import Setting
from instance import Instance

# Almacenamiento de datos

app = Flask(__name__)

CORS(app)

# Declaracion de objetos
Users = []
Resources = []
Categories = []
Settings = []
Instances = []

# Datos ingresados
Users.append(User(1,'Angel', '55555-9', '5-55 zona Roja', 'angel@email.com', 'root', 'root', 1))
Users.append(User(2,'Geovanny', '55555-8', '5-56 zona Roja', 'geo@email.com', 'geo', 'geo', 1))

Resources.append(Resource(1, 'Nucleo A', 'CPU', 'Ghz', 'Procesamiento', 0.03, 1))

Categories.append(Category(1, 'Inter', 'Ejemplo de una descripción', 'Medio'))

Settings.append(Setting(1, 'Default', 'Configuración por default', 'Dim', 50, 1))

Instances.append(Instance(1, 'WebApp CAT', 'Vigente', '10/06/2022 13:13', '02/11/2022 13:13', 1, '55555-8'))

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

    return (answer)

# Post user
@app.route('/users', methods=['POST'])
def insertUser():
    global Users

    new = User(
        request.json['id'],
        request.json['name'],
        request.json['nit'],
        request.json['address'],
        request.json['email'],
        request.json['username'],
        request.json['password'],
        request.json['user_type']
    )
    Users.append(new)
    answer = jsonify({'message': 'Added user'})

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

# --------------- Resource ---------------

# Get resource
@app.route('/resources', methods=['GET'])
def selectAllResources():
    global Resources
    Data = []

    for resource in Resources:
        Fact = {
            'id': resource.getId(),
            'name': resource.getName(),
            'abbreviation': resource.getAbbreviation(),
            'metrics': resource.getMetrics(),
            'type': resource.getType(),
            'worth': resource.getWorth()
        }
        Data.append(Fact)
    
    answer = jsonify({'resources': Data})

    return (answer)

# Post resource
@app.route('/resources', methods=['POST'])
def insertResource():
    global Resources

    new = Resource(
        request.json['id'],
        request.json['name'],
        request.json['abbreviation'],
        request.json['metrics'],
        request.json['type'],
        request.json['worth'],
        request.json['id_config']
    )
    Resources.append(new)
    answer = jsonify({'message': 'Added resource'})

    return (answer)

# --------------- Category ---------------

# Get categoies
@app.route('/categories', methods=['GET'])
def selectAllCategories():
    global Categories
    Data = []

    for category in Categories:
        Fact = {
            'id': category.getId(),
            'name': category.getName(),
            'description': category.getDescription(),
            'load': category.getLoad()
        }
        Data.append(Fact)
    
    answer = jsonify({'categories': Data})

    return (answer)

# Post Category
@app.route('/categories', methods=['POST'])
def insertCategory():
    global Categories

    new = Category(
        request.json['id'],
        request.json['name'],
        request.json['description'],
        request.json['load']
    )
    Categories.append(new)
    answer = jsonify({'message': 'Added category'})

    return (answer)
    
# --------------- Setting ---------------

# Get settings
@app.route('/settings', methods=['GET'])
def selectAllSettings():
    global Settings
    Data = []

    for setting in Settings:
        Fact = {
            'id': setting.getId(),
            'name': setting.getName(),
            'description': setting.getDescription(),
            'dimensional': setting.getDimensional(),
            'cost': setting.getCost(),
            'id_category': setting.getId_category()
        }
        Data.append(Fact)
    
    answer = jsonify({'settings': Data})

    return (answer)

# Post Setting
@app.route('/settings', methods=['POST'])
def insertSetting():
    global Settings

    new = Setting(
        request.json['id'],
        request.json['name'],
        request.json['description'],
        request.json['dimensional'],
        request.json['cost'],
        request.json['id_category']
    )
    Settings.append(new)
    answer = jsonify({'message': 'Added setting'})

    return (answer)

# --------------- Instance ---------------

# Get instaces
@app.route('/instances', methods=['GET'])
def selectAllInstances():
    global Instances
    Data = []

    for instance in Instances:
        Fact = {
            'id': instance.getId(),
            'name': instance.getName(),
            'condition': instance.getCondition(),
            'start': instance.getStart(),
            'end': instance.getEnd(),
            'id_config': instance.getId_config(),
            'id_user': instance.getId_user()
        }
        Data.append(Fact)
    
    answer = jsonify({'instances': Data})

    return (answer)

# Post Instance
@app.route('/instances', methods=['POST'])
def insertInstane():
    global Instances

    new = Instance(
        request.json['id'],
        request.json['name'],
        request.json['condition'],
        request.json['start'],
        request.json['end'],
        request.json['id_config'],
        request.json['id_user']
    )
    Instances.append(new)
    answer = jsonify({'message': 'Added instance'})

    return (answer)

# --------------- FIN RUTAS ---------------

# Para que se ejecute el API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)