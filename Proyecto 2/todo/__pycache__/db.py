#Se importa la librería mysql.connector para manejar la conexión a la base de datos MySQL
import mysql.connector
#se importa la librería click para crear comandos de línea de comandos
import click
from flask import current_app, g
#sirve para vincular funciones a la aplicación Flask o variables de contexto
from flask.cli import with_appcontext
from .schema import instructions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOTS'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c=g.db.cursor(dictionary=True)
    # con este retorno se devuela la conexion a la base de datos y el cursor
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    