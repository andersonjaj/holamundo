#class Usuario: 
  #  nombre= "Junior"
 #   apellido= "Petit"

#usuario = Usuario()

#print(usuario.nombre, usuario.apellido)

# class Usuario:
#    def __init__(self, nombre, apellido):
#         self.nombre= nombre
#         self.apellido= apellido

#aqui ejecutamos la clase Persona y anexamos el metodo de saludar para luego ejecutarlo
# class Persona:
#     def __init__(self, nombre, edad):  # método constructor
#         self.nombre = nombre            # atributo
#         self.edad = edad                # atributo

#     def saludar(self):                  # método (acción)
#         print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
#     def saludar2(self):                 #metodo(accion 2)
#         print("hola, soy", self.nombre)

# p1 = Persona("Junior", 25)
# p1.saludar()
# p1.saludar2()

#DEMOSTRACION DE HERENCIA
# class Persona:
#     def __init__(self, nombre, edad):  # método constructor
#         self.nombre = nombre            # atributo
#         self.edad = edad                # atributo

#     def saludar2(self):                 #metodo(accion 2)
#         print("hola, soy", self.nombre)

# class Admin(Persona):
#     def nuevosaludo(self):
#         print ("Soy un nuevo administrador y mi nonombre es",self.nombre,"y tengo",self.edad," a;os de edad")

# p1= Admin("Junior",35)
# p1.saludar2()
# p1.nuevosaludo()

#como extender __init__
class Gato:
    def __init__(self,nombre,onomatopeya):
        self.nombre=nombre
        self.onomatopeya=onomatopeya
    def saludo(self):
        print("Hola, soy un felino y mi sonido es el ",self.onomatopeya)

class Leon(Gato):
    def __init__(self,nombre,onomatopeya,patas):
        super().__init__(nombre,onomatopeya)
        self.patas=patas
    def metodo(self):
        print("Soy ",self.nombre," y soy un felino con ",self.patas)

p1=Leon("Simba","GRRR",4)
p1.metodo()

