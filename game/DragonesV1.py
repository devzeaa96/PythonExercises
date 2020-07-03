import random
import time

play = 1
cont = 0

def introduction():
    print('''   Estás en una tierra llena de dragones. Frente a tí
    hay dos cuevas. En una de ellas, el dragón es generoso y amigable
    y compartirá su tesoro contigo. El otro dragón
    es codicioso y está hambriento, y te devorará inmediatamente.
    ¿A qué cueva quieres entrar? (1 ó 2)''')
    user =  int(input())
    return user

def choice():
    dragon = random.randint(1, 2)
    return dragon

def steps ():
    print ('¿Asustado?')
    time.sleep(2)
    print('Está muy oscuro ¿verdad?')
    time.sleep(3)
    print(' YA CASI LLEGAS')

while play == 1:
    cont += 1
    u = introduction()
    d = choice()
    print('user ',str(u))
    print('dragon ',str(d))
    steps()

    if u == d:
        print ('*******************************')
        print ('************Muerto*************')
        play = int(input('Volver a jugar 1 para si, o 2 para no'))
    else:
        print ('----------------------------------')
        print ('-----------Felicitaciones---------')
        play = 0
else:
    print('Numeros de intentos ',str(cont))
    print('Bye')