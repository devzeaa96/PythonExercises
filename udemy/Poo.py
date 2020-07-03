class Auto:
    Rojo = False
    Puertas = False
    Gasolina = False
    Vidrios = True

    def __init__(self, doors = None, color = None):
        self.doors = doors
        self.color = color
        if doors is not None and color is not None:
            print('Se creo un auto de color {} y cantidad de puertas {} '.format(color, doors))
    
    def Fabricar(self):
        self.Rojo = True
    
    def confirmar_fabricacion(self):
        if self.Rojo:
            print('Auto coloreado')
        else:
            print('Aun no esta coloreado')
    
    def ContPuertas(self):
        if self.Puertas:
            print('Tiene puertas')
        else:
            print('No tiene puertas')
            try:
                print('Quiere que tenga puertas ingrese un numero')
                a = int(input())
                if a == 1:
                    self.Puertas = True
            except:
                print ('Debe ingresar un valor')
    
    def Galones(self):
        self.Gasolina = True
        while self.Gasolina == True:
            try:
                print('Cuantos galones deseas que tenga el carro: ')
                g = int(input())
                if g >= 25:
                    print('El carro tendra ', str(g*10), 'caballos de fuerza')
                elif g >= 20:
                    print('El carro tendra ', str(g*9), 'caballos de fuerza')
                elif g >= 10:
                    print('El carro tendra ', str(g*5), 'caballos de fuerza')
                else:
                    print('El carro tendra ', str(g*2), 'caballos de fuerza')

            except:
                print('Ingrese un numero')
            else:
                self.Gasolina = False
                print('Gracias')


        
a = Auto(4, 'Azul')
#a.confirmar_fabricacion()
#a.Fabricar()
#a.confirmar_fabricacion()
#a.ContPuertas()
#a.ContPuertas()
#a.Galones()