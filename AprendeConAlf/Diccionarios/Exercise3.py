dicc =  {'Plátano': 1.35,'Manzana': 0.80,'Pera': 0.85,'Naranja':0.70}

fruit = input('Ingrese la fruta: ')

if fruit in dicc:
    kl = int(input('Cuantos kilos : '))
    precio =  kl * dicc[fruit]
    print('Para la fruta ', fruit, 'el precio es : ', precio)