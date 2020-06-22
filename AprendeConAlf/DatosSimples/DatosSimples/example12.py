a = float(input('Ingrese el valor a consignar en la cuenta: '))
porc = a*0.04

print('En el primer año: ', str(round(a+porc, 2)), '\n',
      'En el segundo año: ', str(round((a+(porc*2)), 2)), '\n',
      'En el tercer año: ', str(round((a+(porc*3)), 2)), '\n')