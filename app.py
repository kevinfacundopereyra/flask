from flask import Flask, request, jsonify
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
def helloworld():
    return('Hello world from the API')

@app.route('/consigna1')
def get_empleados():
    cur = mysql.connection.cursor()
    cur.execute('SELECT apellido FROM empleados')
    data = cur.fetchall()
    cur.close()
    print(data)
    
    empleados = [ {'apellido': row[0]} for row in data ]
    return jsonify({'empleados': empleados} )

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
    
if (__name__) == '__main__' :
    app.run(port=3000, debug=True)

