import random
import time


def finish():
    print ('Bye')
    print ('Intentos realizados ')
    
def steps ():
    print ('¿Asustado?')
    time.sleep(2)
    print('Está muy oscuro ¿verdad?')
    time.sleep(3)
    print(' YA CASI LLEGAS')
    
def ingreso():
    print ('''Estás en una tierra llena de dragones. Frente a tí hay dos cuevas. En una de ellas, el dragón es generoso y amigable
    y compartirá su tesoro contigo. El otro dragón es generoso y amigable y compartira su tesoro contigo. 
    El otro dragón es codicioso y hambriento , y te devorará inmediatamente.''')
    user = int(input('Ingrese a cual cueva deseas entrar'))
    return user

def evil():

    print ('''MUERTO, El dragón te ha engullido''')
    print ('¿Quieres seguir jugando?')
    access = int(input('1 para volver a intentarlo'))

    if access == 1:
        print ('¿Quieres seguir jugando?')
        print ()
        inicio()
    else:
        finish()

def good():
    print('Eureca!!!!')
    print('El dragón ha sido amable y entrego todo su tesoro')
    finish()
    

def inicio():
    user = ingreso()

    dragon = random.randint(1, 2)

    print(dragon)

    steps()

    if dragon == user:
        evil()
    else:
        good()

inicio()
    





