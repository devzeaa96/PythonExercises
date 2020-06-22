num = int(input('Ingrese un numero: '))
hola = []
var = 1
for i in range(num):
    if var%2 == 1:
        hola.append(var)
    var += 1

print(hola)

n = int(input('Introduce un número entero positivo: '))

for i in range(1, n+1, 2):
    print(i, end=", ")