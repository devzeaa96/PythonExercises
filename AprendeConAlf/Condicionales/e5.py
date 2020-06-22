age = int(input('Ingrese su edad: '))
income = float(input('Cuanto son sus ingresos: '))

if age >= 16 and income >1000:
    print('Debe tributar')
else:
    print('No debe tributar')