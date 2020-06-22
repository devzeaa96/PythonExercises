num = int(input('Ingrese un numero: '))
a = 0
div = 2
while a != 1:
    var = num%div
    if var == 0:
        print('No es primo')
        if div >= num:
            a =1
    else:
        print('Numero primo')
        a=1
    div += 1

   
   
   
   

            