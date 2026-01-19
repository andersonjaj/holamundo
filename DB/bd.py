import mysql.connector

midb=mysql.connector.connect(
    host="localhost",
    user="Cypherth",
    password="19121991as",
    database="prueba"
)

cursor=midb.cursor();

cursor.execute('select * from usuario')

resultado = cursor.fetchall()

print(resultado)