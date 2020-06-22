a = float(input('Ingrese el valor a invertir :'))
b = float(input('Ingrese el tiempo en años :'))
c = int(input('Ingrese el interes :'))

print('El valor del capital obtenito es ', str(round(a*(c/100+1)**b, 2)))
