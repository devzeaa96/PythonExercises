class Factory:
    def __init__(self, name, time, wheels):
        self.name = name
        self.time = time
        self.wheels = wheels
        print('Se creo un auto', self.name)
    
    def __str__(self):
        return "{} se fabrico con exito, en el tiempo {} y tiene una cantidad de reudas {}".format(self.name, self.time, self.wheels)

    def __del__(self):
        print('Se elimino auto', self.name)

a = Factory('Pedro', 5, 8)
print (str(a))

