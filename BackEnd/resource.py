'''
*Recurso (Resource)
- id (id)
- nombre (name)
- abreviatura (abbreviation)
- métrica (metrics)
- tipo (type)
- valor (worth)
'''

class Resource:
    
    def __init__(self, id, name, abbreviation, metrics, type, worth):
        self.id = id
        self.name = name
        self.abbreviation = abbreviation
        self.metrics = metrics
        self.type = type
        self.worth = worth

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
    
    # abbreviation
    def getAbbreviation(self):
        return self.abbreviation
    
    def setAbbreviation(self, abbreviation):
        self.abbreviation = abbreviation
    
    # metrics
    def getMetrics(self):
        return self.metrics

    def setMetrics(self, metrics):
        self.metrics = metrics

    # type
    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type
    
    # worth
    def getWorth(self):
        return self.worth
    
    def setWorth(self, worth):
        self.worth = worth