price = [ 50, 75, 46, 22, 80, 65, 8]

Menor = price[0]
Mayor = price[0]

for a in price:
    if a < Menor:
        Menor = a
    if a > Mayor:
        Mayor = a
        
print("El numero mayo es: ", Mayor, "\nEl numero menos es :", Menor)