#libreria os permite interactuar con el sistema operativo
import os

#iomportar Flask lo cual es necesario para crear una aplicacion web
from flask import Flask

def create_app():
    #crear una instancia de la aplicacion Flask
    app = Flask(__name__)

    #configurar la clave secreta para la aplicacion, auyda a proteger los datos de la aplicacion y las sesiones de los usuarios
    app.config.from_mapping(
        SECRET_KEY= 'mikey',
        DATABASE_HOTS=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
        )
    from . import db
    #inicializar la base de datos con la aplicacion y cerrar la conexion a la base de datos cuando la aplicacion se cierra
    db.init_app(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    return app