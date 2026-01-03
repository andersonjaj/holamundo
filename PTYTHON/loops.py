# Example of a while loop in Python
i=0
#while i < 5:
#    print(i)
#    i+= 1

# while i<5:
#     print(i)
#     if i==3:
#         #break cierr
#         break
#     i+=1

# for x in range(3,30):
#     print(x)
# else:
#     print("El ciclo for ha terminado")

# usuarios = ["Ana", "Luis", "Carlos", "Marta"]
# edades = [23, 30, 18, 25]

# for usuario in usuarios:
#     for edad in edades:
#         print(usuario,edad)

# def mifuncion():
#     print("mi primera fiuncion")

# mifuncion()

# def funcion(*apellido):
#     print("Mi nombre completo es:", apellido[0])

# funcion("Carlos", "Rodriguez")


#FUNCION CON LISTA 

# def funcion2(lista):
#     for el in lista:
#         print(el)

# funcion2(["Junior","Andrea","Felipe"])

# def concatenarnombres(lista):
#     i=""
#     for el in lista:
#         i=i+" "+el
#     return i

# concat=concatenarnombres(["Junior","Andrea","Felipe"])
# print(concat)

def recursion(i):
    if(i<1):
        return 1
    print(i)
    recursion(i-1) 

recursion(6)