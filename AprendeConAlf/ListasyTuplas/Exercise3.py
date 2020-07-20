asig = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
nota = []
for i in asig:
    print('Ingrese la nota de la asignatura para ', i, ':')
    nt = float(input())
    nota.append(nt)
    
print(nota)  

for i in range(0,4):
    print('En ', asig[i], 'has sacado', nota[i])