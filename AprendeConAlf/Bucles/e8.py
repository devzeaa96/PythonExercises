var = int(input('Ingrese un numero: '))

for i in range (1, var+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()