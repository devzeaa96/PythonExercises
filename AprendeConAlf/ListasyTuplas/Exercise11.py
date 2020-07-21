a = (1,2,3)
b = (-1,0,2)

producto = (a[0]*b[0])+(a[1]*b[1])+(a[2]*b[2])

print("El producto escalar es : ", producto)

a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 