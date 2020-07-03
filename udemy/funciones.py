def hola(arg):
    print('Hola ',arg)

print('Ingrese su nombre: ')
nombre= input()
hola(nombre)

def saludo(arg1, arg2):
    print('Hola soy ', arg1, 'y tu eres ', arg2)

print('Ingrese el valor 1: ')
nombre1= input()
print('Ingrese el valor 2: ')
nombre2= input()

saludo(arg2=nombre1, arg1=nombre1)

#def llenar(lista):
#    i= 0
#    for recorrer in lista:
#        lista[i]= input('ingrese un valor')
#        i +=1
#    return lista

itera= int(input('ingrese el numero de iteraciones'))
#lista1 = llenar(itera)
lista2= []
#len(lista2)= itera
#llenar(lista2)
print(lista2)
i= 1
def llenarlista(itera, i):
    while i <= itera:
        print('Ingrese el valor en la posicion ', str(i), ':')
        lista2.append(int(input()))
        i += 1
llenarlista(itera, i)
print(lista2)
