punt = float(input('ingrese su puntuación: '))
price = 2400

if punt == 0:
    print('Valor a recibir: ',price)
elif punt == 0.4:
    price = price + (price*punt)
    print('Valor a recibir con el 4 : ',price)
elif punt >= 0.6:
    price = price + (price*punt)
    print('Valor a recibir con el 6 : ',price)    