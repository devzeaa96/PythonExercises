avar = [(1,2,3),
     (4,5,6)]
b = [(-1,0),
     (0,1),
     (1,1)]

b1 = []
b2 = []
a1 = []
a2 = []

i = 1
for e in b:
    for a in e:
        if i == 1:
            b1.append(a)
            i=0
        else:
            b2.append(a)
            i=1
   
i = 0
for r in avar:
    for t in r:
        if i <= 2:
            a1.append(t)
            i=i+1
        else:
            a2.append(t)


print("b1", b1)
print("b2", b2) 
print("a1", a1)
print("a2", a2)

c11 = c12 = c21 = c22 = i = 0
for ter in a1:
    c11=  c11+ (ter*b1[i])
    c12=  c12+ (ter*b2[i])
    i=i+1
i = 0
for teri in a2:
    c21=  c21+ (teri*b1[i])
    c22=  c22+ (teri*b2[i])
    i=i+1

Matriz = [[c11, c12], [c21,c22]]

print(Matriz)

""" Solución mas corta """

a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])