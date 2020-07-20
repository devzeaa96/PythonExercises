materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
n = []

for i in materias:
    print('Ingrese la nota en la asignatura:', i)
    nota = float(input())
    if nota < 3.0:
        n.append(i)

print ('Tienes que repetir',n)


            