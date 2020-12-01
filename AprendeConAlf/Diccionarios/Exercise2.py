nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
direcc = input('Ingrese su dirección: ')
telefono = input('Ingrese su telefono: ')

dicc = {'Nombre':nombre, 'Edad': edad, 'Direccion':direcc, 'Telefono': telefono}

print(dicc['Nombre'], ' tiene', dicc['Edad'], ', vive en ', dicc['Direccion'], 'y su numero telefonico es : ', dicc['Telefono'])