dicc = {'Euro': '€', 'Dollar':'$', 'Yen':'¥'}

opcion = input('Ingrese la moneda a buscar: ')

     if opcion in dicc:
    print('Modena: ', dicc[opcion])
else:
        print('No tengo esa moneda')
        
''' for a in dicc:
    if opcion == a:
        print('Modena: ', dicc[opcion])
    else:
        print('No tengo esa moneda') '''
        
currencies = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency = input("Introduce una divisa: ")
print(currencies.get(currency.title(), "La divisa no está."))