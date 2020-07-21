word = input('Ingrese una palabara: ')
a = len(word)

orin = []
reve = []

for i in range(0,a):
    orin.append(word[i])
    reve.append(word[i])

reve.reverse()
acum = 0
t=0
for e in orin:
    if e == reve[t]:
        acum=acum+1
    t=t+1
   
if a == acum:
    print("La palabra es un palíndromo")
else:
    print("No es palindromo")
    

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
    