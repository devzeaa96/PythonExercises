name = input('Ingrese el nombre: ')
num = int(input('Ingrese el numero de veces a mostrar: '))

for i in range(num):
    print(name)
    
print('Second')
print((name + "\n") * int(num))