#########################TUPLAS##########################
t = (1, 4, 2, 3, 'Tupla', 1, 1, 1)
print(t)

# t.app(0)
# t.append(8)

print(t.index('Tupla'))
print(t.index(1))
v = len(t)
print (v)


#########################CONJUNTOS#######################
con = {1, 2, 3, 4}
print(con)
con.add('Hola')
con.add('Noo')
con.add(1)
con.add(80)

print(con)

v = len(con)
print (v)

#########################DICCIONARIOS####################

dic = {'David':'Desarrollado','Vanessa':'Lider - soporte', 'Cesar':'Gerente'}
print(dic)
print(dic['David'])
i=0
for recorrer in dic:
    print(recorrer, dic[recorrer])
    i += 1

#########################PILAS###########################

p= [1, 2, 3, 4, 5, 6]
print(p)
v = len(p)
while  v > 0:
    p.pop()
    print(p)
    v = len(p)
else:
    i='Hola'
    p.append(i)
    print(p)

#########################COLAS###########################

from collection import deque
ol = deque()


