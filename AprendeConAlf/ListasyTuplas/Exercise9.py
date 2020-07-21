word = input('Ingrese una palabra: ')

asd = list(word)

a, e, i, o, u = 0, 0, 0, 0, 0

for f in asd:
    if f == "a":
        a=a+1
    if f == "e":
        e=e+1
    if f == "i":
        i=i+1
    if f == "o":
        o=o+1
    if f == "u":
        u=u+1

print('La pablra: ', word, 'tiene vocales, \na: ',a,'\ne: ',e,'\ni: ',i,'\no: ',o,'\nu: ',u)


word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")