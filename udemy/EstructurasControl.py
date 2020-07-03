import random
#################################IF#####################################
if True:
    print ('True')

nombre = input('Ingrese su nombre')
if nombre == '':
    print ('Ingrese un valor difente a vacio')

numero = int(input('Ingrese el numero que vamos a validar'))
numero2 = random.randint(0,3)
print (numero2)
if numero == numero2:
    print ('El numero es igual')

print ('Gracias')

lista = [1,2,2,3,4,5,6,7,8,9,0]
print(len(lista))

lista.append(10)

print(lista)

if len(lista) == 12:
    print ('La lista tiene 12 valores')
    lista.append(20)
print(lista)

if lista[1] == 1:
    print ('El valor es 1')

##################################ELSE####################################

n4 = random.randint(0,30)
numero3 = int(input('Ingrese el valor que desea comparar'))

if n4 == numero3:
    print('Los numero son iguales', str(numero3), '<-- Usuario vs PC -->', str(n4))
else:
    print('Los numeros no son iguales', str(numero3), '<-- Usuario vs PC -->', str(n4))

if lista[0] == 1:
    print('Son iguales')
else:
    print('Son diferentes')
####################################ELIF##################################
print(n4)
if n4 >= 30:
    print('Puntaje maximo')
elif n4 >= 25:
    print('Puntaje sobresaliente')
elif n4 >= 20:
    print('Puntaje bueno')
elif n4 >=15:
    print('Puedes mejorar')
elif n4>=10:
    print('Hay varias cosas por mejorar')
elif n4 >= 5:
    print('No cumples con los logros propuesros')
else:
    print('Carita llorando')

#####################################WHILE################################
n4 = random.randint(0,40)
while n4 <= 30:
    if n4 >= 30:
        print('Puntaje maximo')
    elif n4 >= 25:
        print('Puntaje sobresaliente')
    elif n4 >= 20:
        print('Puntaje bueno')
    elif n4 >=15:
        print('Puedes mejorar')
    elif n4>=10:
        print('Hay varias cosas por mejorar')
    elif n4 >= 5:
        print('No cumples con los logros propuesros')
    elif n4 >= 0:
        print('Carita llorando')
    n4 = random.randint(0,40)
else:
    print('numero mayor a 30', n4)

######################################FOR#################################

for recorrer in lista:
    print(str(recorrer))

indice = 0

for recorrer in lista:
    lista[indice] = lista[indice] * 10
    print(str(lista[indice]))
    indice += 1
