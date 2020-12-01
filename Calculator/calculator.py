#Caluclator 

a = 1
b = 2
result = 0


o = input("Ingrese la operación que va a realizar: ")
ope = ""

if o == "+":
    result = a + b
    ope = "suma"
    
if o == "-":
   result = a - b 
   ope = "resta"
   
if o == "*":
    result = a * b
    ope = "multiplicacion"

if o == "/":
    result = a / b
    ope = "Division"

print("Resultado : ", result, "la oepracion fue ",ope)
    
    
    
    