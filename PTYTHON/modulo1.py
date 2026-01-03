import modulos
from camelcase import CamelCase
# print(modulos.mascotas)
# modulos.saludo("juan")

# from modulos import saludo, mascotas

# print(mascotas)
# saludo("juan")

c = CamelCase()
s="esta oracion necesita calmcase"

camelcased= c.hump(s)
print(camelcased)