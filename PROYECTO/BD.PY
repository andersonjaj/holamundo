#luego de instalar mysql-connector-python llamamos al modulo
import mysql.connector

#creamos la conexion a la base de datos, indicando host, user, password y database
midb=mysql.connector.connect(
    host="localhost",
    user="Cypherth",
    password="19121991",
    database="proyecto"
)

#LISTAR DATOS
#creamos el cursor para ejecutar las consultas
# cursor=midb.cursor()
# #ejecutamos la consulta
# #solicitamos que nos muestre todos los registros de la tabla aprendices
# cursor.execute('select * from aprendices')
# #obtenemos el resultado
# resultado = cursor.fetchall()

# print(resultado)


# #INSERTAR DATOS
#creamos el cursor para ejecutar las consultas
cursor=midb.cursor()
#creamos la consulta SQL y los valores a insertar
sql='insert into aprendices (cedula, nombre, apellido, sexo, fecha_nacimiento, estatus) values (%s, %s, %s, %s, %s, %s)'
values=(12345678, 'Junior', 'Petit', 'M', '1991-12-19', 'activo')

#ejecutamos la consulta
cursor.execute(sql, values)
#confirmamos los cambios en la base de datos
midb.commit()
#mostramos cuantos registros fueron insertados
print(cursor.rowcount, "registro insertado.")

# # #ACTUALIZAR DATOS
# #creamos el cursor para ejecutar las consultas 
# cursor=midb.cursor()
# #creamos la consulta SQL y los valores a actualizar
# sql='update aprendices set nombre = %s, apellido = %s, cedula = %s where id_aprendices = %s'
# Values=('Anderson', 'Ollarvides', 19967449, 1)
# cursor.execute(sql, Values)
# #confirmamos los cambios en la base de datos
# midb.commit()
# #mostramos cuantos registros fueron actualizados    
# print(cursor.rowcount, "registro actualizado.")

#ELIMINAR DATOS
# sql='delete from aprendices where id_aprendices = %s'
# #SE LE ASIGNA EL VALOR DEL ID A ELIMINAR EN FORMA DE TUPLA
# valoreliminar=(1,)
# cursor.execute(sql, valoreliminar)
# #confirmamos los cambios en la base de datos
# midb.commit()
# #mostramos cuantos registros fueron eliminados    
# print(cursor.rowcount, "registro eliminado.")