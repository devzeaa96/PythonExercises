class Factory:
    def __init__(self, mark, name, price, description):
        self.mark = mark
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return """
        Marca \t\t {}
        Nombre \t\t {}
        Precio \t\t {}
        descrption \t {}""".format(self.mark, self.name, self.price, self.description)

class Auto(Factory):
    pass

z = Auto('Ford', 'Fiesta', 10000, 'Automovil')
print(z)


class Deportivo1(Factory):
    wheels = ''
    distributor = ''

    def __str__(self):
        return """
        Marca \t\t {}
        Nombre \t\t {}
        Precio \t\t {}
        descrption \t {}
        Ruedas \t\t {}
        Distributor \t {}""".format(self.mark, self.name, self.price, self.description, self.wheels, self.distributor)

deportivo = Deportivo1('Mecedez' , 'A500', 500000, 'Deportivo')
deportivo.wheels = 5
deportivo.distributor = 'Autocar'

print(deportivo)