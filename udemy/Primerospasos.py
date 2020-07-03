variable = 'cadena \n \n david'
print(type(variable))
print(variable)
print(r'afgasfdgcadena \n \n david')

cadena = """Hola 

soy 

una cadena"""
print (cadena)

cadena2 = '''T
a
m
b
ien soy una cadena'''
print (cadena2)

print ('Utilicemos tuna ****** \t *********')
print ('David \t Zea\n Acosta\t Luis')

print (variable[0:5])
print (variable[:5] + variable[-5:])

print (len(variable))

print (variable[0])

###################################################################################

lista =[5, 6, 'david', -4, 'prueba']
print (lista)

print (str(lista[0]) +'\t'+ lista[4])

lista[0] = 'cambio'

print (str(lista[3]))
print (lista)
print (lista[:3])
print (lista[3:])

lista2 = [2, 6, 4, -8, 9]
lista3 = [6, 9, 8, 7, 9]

print (lista2 + lista3)

print (str(lista2[0]+lista3[1]))

lista2 [:3] = [10,30,100] 
print (lista2)

lista2[0] ='Cadena'
print (lista2)

lista2.append('Cadena')
print (lista2)

#################################################################################

ingreso = input('Ingrese el numero \t')
print ('\t'+ingreso)

numero1 = 5
numero2 = 5.5

suma = numero1 + numero2
print (suma)

numero3 = float(input('Ingresa el valor de que desea sumar'))
suma = numero3 + numero2
print (str(suma))

numero4 = int(input('ingrese el valor que va a sumar'))
suma = numero3 + numero4
print (suma)   
