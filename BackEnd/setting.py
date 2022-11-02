'''
*Configuración (Setting)
- id (id)
- nombre (name)
- descripción (description)
- dimensional (dimensional)
- costo (cost)
- id_categoria (id_category)
'''

class Setting:

    def __init__(self, id, name, description, dimensional, cost, id_category):
        self.id = id
        self.name = name
        self.description = description
        self.dimensional = dimensional
        self.cost = cost
        self.id_category = id_category
    
    # Metodos GET y SET
    # id
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    # name
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    # description
    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    # dimensiona
    def getDimensional(self):
        return self.dimensional
    
    def setDimensional(self, dimensional):
        self.dimensional = dimensional
    
    # cost
    def getCost(self):
        return self.cost
    
    def setCost(self, cost):
        self.cost = cost

    # id_category
    def getId_category(self):
        return self.id_category

    def setId_category(self, id_category):
        self.id_category = id_category