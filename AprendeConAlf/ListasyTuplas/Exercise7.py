abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
       "z"]

mult = []

i = 1
for a in abc:
    if i % 3 == 0:
        mult.append(abc[i-1])    
    i=i+1

print(mult)

for a in abc: 
    for l in mult:
        if l == a:
            abc.remove(l)

  
print(abc)
