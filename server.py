from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os 

app = Flask(__name__)


app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL()

mysql.init_app(app) 

@app.route('/')
def home():
        cur = mysql.connection.cursor()
        cur.execute('SELECT apellido, nombre FROM empleados')
        data = cur.fetchall()
        cur.close()
        
        empleados =  [{'apellido': row[0],                        
                       'nombre': row[1]}
                      for row in data]
        
        return jsonify({'mensaje': 'Datos traidos con exito!', 'empleados': empleados})

@app.route('/agregarempleado', methods=['POST'])
def agregar_empleado():
    try:
        data = request.get_json()  
        apellido = data['apellido']
        nombre = data['nombre']
        pais = data['pais']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO empleados (apellido, nombre, pais) VALUES (%s, %s, %s)', (apellido, nombre, pais))
        mysql.connection.commit()
        cur.close()

        return jsonify({'mensaje': 'Empleado agregado correctamente'})
    
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/actualizarempleado/<int:id>', methods=['PUT'])
def actualizar_empleado(id):
    try:
        data = request.get_json()
        apellido = data.get('apellido')
        nombre = data.get('nombre')
        pais = data.get('pais')

        cur = mysql.connection.cursor()
        cur.execute('UPDATE empleados SET apellido = %s, nombre = %s, pais = %s WHERE id = %s', (apellido, nombre, pais, id))
        mysql.connection.commit()
        cur.close()

        return jsonify({'mensaje': 'Empleado actualizado correctamente'})
    
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/eliminarempleado/<int:id>', methods=['DELETE'])
def eliminar_empleado(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM empleados WHERE id = %s', (id,))
        mysql.connection.commit()
        cur.close()

        return jsonify({'mensaje': 'Empleado eliminado correctamente'})
    
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/empleados/<string:pais>')
def empleados(pais):
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre, apellido FROM empleados WHERE pais= %s', (pais,))
    data = cur.fetchall()
    cur.close()
    
    empleados = [ { 'apellido': row[1],
                    'nombre': row[0]} 
                 for row in data]
    
    return jsonify({'mensaje': 'Datos traidos exitosamente!'}, { 'empleados': empleados })
    


if __name__ == '__main__':
    app.run(port=3000, debug=True)
