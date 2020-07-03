class Student:

    def __init__(self, name, note):
        self.name = name
        self.note = note
        print('Estudiante creado')
    
    def show(self):
        print('El estudiante es : ', self.name, 'su nota es ', str(self.note))

    def __str__(self):
        while True:
            try:
                if  self.note <= 10:
                    if self.note >= 9:
                        return print('El estudiante tiene una nota Excelente')
                    elif self.note >= 7:
                        return print('El estudiante tiene una nota Sobresaliente')
                    elif self.note >= 5:
                        return print('El estudiante tiene una nota Buena')
                    elif self.note >= 3:
                        return rint('El estudiante tiene una nota Mala')
                    else:
                        return print('El estudiante tiene una nota Muy Mala')
                    break
            except:
                return print ('Debes ingresar un valor menor a o igual a 10')

n = input('Ingrese el nombre del estudiante')
print ('Ingrese la nota de', n)
n2 = int(input())
a = Student (n, n2)
a.show()
a.__str__()