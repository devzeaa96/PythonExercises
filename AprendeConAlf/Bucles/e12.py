var = input('Ingrese la una frase: ')
letter = input('Ingrese una letra: ')
cont = 0
for i in var:
    if letter == i:
        cont +=1
        
print('La letra ', letter, 'esta ',cont)