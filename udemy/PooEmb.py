class Factory:
    def __init__(self, name, time, wheels):
        self.name = name
        self.time = time
        self.wheels = wheels
        print('Se creo un auto', self.name)
    
    def __str__(self):
        return "{} ({}) s".format(self.name, self.time)

class List:

    autos = []

    def __init__(self, autos):
        self.autos = autos
    
    def fabricar(self, x):
        self.autos.append(x)
    
    def visualizar(self):
        for x in self.autos:
            print (x)

a = Factory('David', 4, 10)
l = List([a])

l.fabricar(Factory('Juan Carlos', 4, 11))
l.fabricar(Factory('Pedro', 4, 4))
l.visualizar()