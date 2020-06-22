inv = float(input('Ingrese el valor a invertir: '))
inter = float(input('Ingrese el interes anual: '))
year = int(input('Cuantos años estara el prestamos: '))

for i in range(year):
    inv = inv + (inv * inter)
    print('En el año ', i+1, ' el capital es: ', inv)
    