#luego de instalar mysql-connector-python llamamos al modulo
import mysql.connector

#creamos la conexion a la base de datos, indicando host, user, password y database
midb=mysql.connector.connect(
    host="localhost",
    user="Cypherth",
    password="19121991as",
    database="prueba"
)
#creamos el cursor para ejecutar las consultas
cursor=midb.cursor();
#ejecutamos la consulta
cursor.execute('select * from usuario')
#obtenemos el resultado
resultado = cursor.fetchall()

print(resultado)