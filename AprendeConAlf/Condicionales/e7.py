var = int(input('Ingrese el valor de su renta anual: '))

if var > 60000:
    var = var + (var*0.45)
    print('El porcentaje será 45% : ', str(var) )
elif var > 35000:
    var = var + (var*0.30)
    print('El porcentaje será 30% : ', str(var))
elif var > 20000:
    var = var + (var*0.20)
    print('El porcentaje será 20% : ', str(var))
elif var > 10000:
    var = var + (var*0.15)
    print('El porcentaje será 15% : ', str(var))
else:
    var = var + (var*0.5)
    print('El porcentaje será 5% : ', str(var))
    
    