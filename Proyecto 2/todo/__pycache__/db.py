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
#importar el cursos y la conexion a la base de datos
def init_db():
    #obtener la conexion a la base de datos y el cursor
    db, c = get_db()
    #iteramos todas las instrucciones definidas en el archivo schema.py
    for instruction in instructions:
        #ejecutamos cada instrucción SQL para crear las tablas necesarias en la base de datos
        c.execute(instruction)
    #se confirman los cambios realizados en la base de datos
    db.commit()
#se define un comando de línea de comandos llamado 'init-db' para inicializar la base de datos
#se ejecuta flask init-db en la terminal para ejecutar este comando
@click.command('init-db')
#permite que la función acceda al contexto de la aplicación Flask
@with_appcontext
#esta función inicializa la base de datos ejecutando las instrucciones definidas en el archivo schema.py
def init_db_command():
    init_db()
    #se imprime un mensaje en la consola indicando que la base de datos ha sido inicializada y a terminado el proceso
    click.echo('Base de datos inicializada.')

def init_app(app):
    app.teardown_appcontext(close_db)
    