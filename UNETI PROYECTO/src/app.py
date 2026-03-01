#importamos la clase Flask del módulo flask y  la función os para manejar rutas de archivos
from flask import Flask, render_template, request, redirect, url_for ,flash
#importamos el módulo mysql.connector para manejar la conexión con la base de datos MySQL y os para manejar rutas de archivos
import os
import mysql.connector
#importamos el módulo database para establecer la conexión con la base de datos
from database import db as db_connection

#creamos una instancia de la clase Flask y le pasamos el nombre del módulo actual como argumento
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#concatenamos la ruta del directorio de plantillas con la ruta relativa de las plantillas
template_dir= os.path.join(template_dir,'src' ,'templates')

#creamos una instancia de la clase Flask y le pasamos la ruta del directorio de plantillas como argumento
app = Flask(__name__, template_folder = template_dir)
#la clave sirve para cifrar los datos de las sesiones y proteger la información del usuario.
app.secret_key="123456789" #clave secreta para usar flash messages

# 1. Ruta de entrada (El Panel Inicial)
@app.route('/')
def login():
    # mostrar página de formulario de aprendices
    return render_template('login.html')

#Ruta para guardar usuarios. indicando el metodo POST ya que se enviarán datos a través de un formulario HTML.
@app.route('/usuario', methods=['POST'])
def addUser():
    cedula = request.form['cedula']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    sexo = request.form['sexo']
    fecha_nacimiento = request.form['fecha_nacimiento']
    cursor = db_connection.cursor()
  
    if cedula and nombre and apellido and sexo and fecha_nacimiento:
        #usamos try para indicar al usuario si la cedula esta registrada y no nos salga un error y cierre la ejecucion
        try:
            sql="INSERT INTO aprendices (cedula, nombre, apellido, sexo, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s)"
            data= (cedula, nombre, apellido, sexo, fecha_nacimiento)
            cursor.execute(sql, data)
            db_connection.commit()

            flash('Usuario registrado exitosamente', 'success')
            return redirect(url_for('gestion'))
        except mysql.connector.Error as err:
            if err.errno==1062:  # Código de error para cedula duplicada
                flash(f"La cédula'{cedula}' ya está registrada', 'error")
            else:
                #para otro errores de mysql
                flash(f'Error al registrar el usuario: ' + {err.msg})
                db_connection.rollback()  # Revertir la transacción en caso de error
            return redirect(url_for('login'))
        finally:
            cursor.close()  # se cierra el cursor en cualquier caso
    else:
        flash("Todos los campos son obligatorios", "info")
        return redirect(url_for('login')) # RETORNO 3 (Campos vacíos)
    
#Esta ruta muestra los aprendices registrados en la base de datos.
@app.route('/gestion')
def gestion():
    cursor=db_connection.cursor()
    # se toman todos los registros de la tabla aprendices y se almacenan en la variable myresult
    cursor.execute("SELECT * FROM aprendices")
    myresult = cursor.fetchall()
    #convertimos los datos a un direccionario
    insertObject = []
    #obtenemos los nombres de las columnas de la tabla aprendices y los almacenamos en una lista llamada columnsanmes
    columnsanmes = [column[0] for column in cursor.description]
    #recorremos cada registro obtenido de la consulta SQL y lo convertimos en un diccionario utilizando la función zip para combinar
    #los nombres de las columnas con los valores de cada registro. Luego, agregamos cada diccionario a la lista insertObject.
    for record in myresult:
        insertObject.append(dict(zip(columnsanmes, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)
    

#Ruta para eliminar usuarios, recibe el id del usuario a eliminar como parámetro en la URL y ejecuta 
# una consulta SQL para eliminar el registro correspondiente en la base de datos.
@app.route('/delete/<int:id_aprendices>')
def delete(id_aprendices):
    cursor = db_connection.cursor()
    #se toma el id de la tabla 
    sql = "DELETE FROM aprendices WHERE id_aprendices = %s"
    data = (id_aprendices,)
    cursor.execute(sql, data)
    db_connection.commit()
    #cerramos el cursor después de ejecutar la consulta para liberar recursos y evitar posibles fugas de memoria.
    cursor.close()
    return redirect(url_for('gestion'))

#ruta para editar informacion de los apnredices tomando como referencia el id d ela fila indicada
@app.route('/edit/<int:id_aprendices>', methods=['POST'])
def edit(id_aprendices):
    # se toman los datos del formulario HTML utilizando request.form y se almacenan en variables correspondientes a cada campo de la tabla aprendices.
    cedula = request.form['cedula']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    sexo = request.form['sexo']
    fecha_nacimiento = request.form['fecha_nacimiento']
    #si se tienen todos los campos se ejecuta la consulta SQL para actualizar el registro correspondiente en la base de datos utilizando 
    # el id_aprendices como referencia. Luego, se redirige al usuario a la página de gestión para mostrar los cambios realizados.
    if cedula and nombre and apellido and sexo and fecha_nacimiento:
        cursor = db_connection.cursor()
        sql = "UPDATE aprendices SET cedula=%s, nombre=%s, apellido=%s, sexo=%s, fecha_nacimiento=%s WHERE id_aprendices=%s"
        data = (cedula, nombre, apellido, sexo, fecha_nacimiento, id_aprendices)
        cursor.execute(sql, data)
        db_connection.commit()
        cursor.close()
        return redirect(url_for('gestion'))

if __name__ == '__main__':
    #indicamos que la aplicacion se ejectute en modo desarrollo y en un puerto específico
    app.run(debug=True, port=4000)