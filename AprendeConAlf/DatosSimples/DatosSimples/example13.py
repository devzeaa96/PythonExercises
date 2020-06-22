bread = 3.49


num = int(input('Cuantas barras vendio que no son del día : '))

bread = bread*num
descount = bread * 0.60

print('El precio habitual es de ', bread, ' Por #', num, 'panes','\n',
      'El descuento es de : ', descount, '\n',
      'El valor total es de: ', str(round(bread-descount, 2)))