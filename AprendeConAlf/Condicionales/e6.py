name = input('Ingrese su nombre: ')
gen = input('ingrese su genero: ')

gen = gen.lower()
letter = name.lower()
letter = letter[0]

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

for i in a:
    if letter == i:
        group = 1
    else:
        group= 2

if gen == 'f' and group == 1:
    print(name, 'pertence al grupo A')
elif gen == 'm' and group == 2:
    print(name, 'pertence al grupo A')
elif gen == 'f' and group == 2:
    print(name, 'pertence al grupo B')
elif gen == 'm' and group == 1:
    print(name, 'pertence al grupo B')



