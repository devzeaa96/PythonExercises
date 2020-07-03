while True:
    try:
        x = int(input('Por favor ingrese un numero: '))
        break
    except ValueError:
        print ('Oops! No era valido. Intente nuevamente')


#import sys

#for arg in sys.argv[1:]:
#    try:
#        f = open(arg, 'r')
#    except IOError:
#        print ('no pude abrir', arg)
#    else:
#        print (arg, 'tiene', len(f.readlines()), 'lineas')
#        f.close()

try:
    print ('Ingrese un numero')
    x= int(input())
except:
    print('No ingresaste un numero')


while True:
    try:
        print ('Ingrese un numero')
        x= int(input())
    except:
        print('No ingresaste un numero')
    else:
        print('Esta es else excepcion ')
        break
    finally:
        print('inicio de sesion')


try:
    a= int(input('Ingrese un numero: '))
    10/a
except TypeError:
    print('Esto es una cadena')
except ValueError:
    print('La cadena debe ser un numero')
except ZeroDivisonError:
    print('El numero no puede ser 0')
except Exception as e:
    print(type(e).__name__)
else:
    print('Este es else')
finally:
    print('Gracias por ingresar')



def fun(estudiantes= None):

        if estudiantes== None:
            raise ValueError('Debes escribiralgo, sino no llames a la funcion')


fun()
             