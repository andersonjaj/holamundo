from flask import Flask, request, url_for
import mysql.connector

mibd = mysql.connector.connect(
    host="localhost",
    user="Cypherth",
    password="19121991",
    database="proyecto"
)

cursor = mibd.cursor()


app = Flask(__name__)
# Definición de rutas de la aplicación Flask y vistas por el usuario
@app.route('/')
def index():
    return "¡Hola, Mundo!"

@app.route('/2daruta')
def segunda_ruta():
    return "¡Esta es la segunda ruta!"