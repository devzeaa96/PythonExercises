
Arreglo = []
var = 0
while var == 0:
    ag = float(input("Ingrese un numero: "))
    Arreglo.append(ag)
    var = int(input("Desea agregar mas numeros: "))
    
acumx2 = acum = 0
for u in Arreglo:
    acum = acum + u

media = acum/len(Arreglo)

print("media :", media)

x2 = []
i = 0
for f in Arreglo:
    x2.append((f-media)**2)

print("(Xi-X)**2", x2)

for d in x2:
    acumx2 = acumx2 + d
    

pp = (acumx2/(len(Arreglo)-1))
    
print('Varianza estandar', pp)


sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)

