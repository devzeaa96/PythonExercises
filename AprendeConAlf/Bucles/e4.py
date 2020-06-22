var = int(input('Ingrese un numero : '))
ri = var
for i in range(var+1):
    print(ri, end=" ,")
    ri -= 1

for i in range(var, -1, -1):
    print(i, end=", ")