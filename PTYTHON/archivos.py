#read = r esto permite leer el archivo viene por defecto
#append =a  agregar mas texto en el archivo
#write = w modificar completamente el archivo
# # x crea un archivo txt con el nombre indicado

# c=open("textoprueba.txt","w")

# # print(c.readline()) #readline lee por linea del archivo entre mas readline 
# #se coloque mas lineas imprimira
# c.write("\nagregando una linea")
# print(c)
# c.close

import os

if os.path.exists("textoprueba.txt")
	os.remove("textoprueba.txt")
else:
	print("el archivo no existe")