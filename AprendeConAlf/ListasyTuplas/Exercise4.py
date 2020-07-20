num = []
ban = True
while (ban == True):
    lot = int(input('Ingrese los numeros ganadores de la loteria: '))
    num.append(lot)
    ban = bool(input('Continuar: '))
    
num.sort()
print(num)