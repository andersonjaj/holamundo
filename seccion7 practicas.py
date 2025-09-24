primero=input("ingrese numero")

try:
    primero=int(primero)
except:
    primero = "ERROR"

segundo=input("ingrese el segundo numero ")

try:
    segundo=int(segundo)
except:
    segundo = "ERROR"

if primero=="ERROR" or segundo == "ERROR" :
    print("INGRESASTE MAL UN DATO")
else:
    print(primero + segundo)
    print(primero)
    print(segundo)