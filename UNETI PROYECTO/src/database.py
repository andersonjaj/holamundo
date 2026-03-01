import mysql.connector
# indicamos los datos de conexión a la base de datos MySQL utilizando mysql.connector.connect() y almacenamos la conexión en la variable db.
# en mi caso llame a mi base de datos proyecto, asi como los demas datos, estos datos deberan der ser ajustados segun la configuración tenga 
db = mysql.connector.connect(
    host="localhost",
    user="Cypherth",
    password="19121991",
    database="proyecto"
)