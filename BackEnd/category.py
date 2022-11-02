'''
*Categoria (Category)
- id (id)
- nombre (name)
- descripción (description)
- carga (load)
'''

class Category:

    def __init__(self, id, name, description, load):
        self.id = id
        self.name = name
        self.description = description
        self.load = load
    
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
    
    # load
    def getLoad(self):
        return self.load
    
    def setLoad(self, load):
        self.load = load