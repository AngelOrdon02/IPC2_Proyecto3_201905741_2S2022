'''
*Instancia (Instance)
- id (id)
- nombre (name)
- estado (condition)
- inicio (start)
- fin (end)
- id_config (id_config)
- id_usuario (id_user)
'''

class Instance:

    def __init__(self, id, name, condition, start, end, id_config, id_user):
        self.id = id
        self.name = name
        self.condition = condition
        self.start = start
        self.end = end
        self.id_config = id_config
        self.id_user = id_user

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

    # condition
    def getCondition(self):
        return self.condition
    
    def setCondition(self, condition):
        self.condition = condition
    
    # start
    def getStart(self):
        return self.start
    
    def setStart(self, start):
        self.start = start
    
    # end
    def getEnd(self):
        return self.end
    
    def setEnd(self, end):
        self.end = end

    # id_config
    def getId_config(self):
        return self.id_config
    
    def setId_config(self, id_config):
        self.id_config = id_config

    # id_user
    def getId_user(self):
        return self.id_user
    
    def setId_user(self, id_user):
        self.id_user = id_user