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
    
@app.route('/agregarproducto/<string:nombre>/<string:descripcion>/<int:precio>/<int:stock>/', methods=['POST'])    
def agregar_producto(nombre, descripcion, precio, stock):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s,%s)', (nombre, descripcion, precio, stock))
    mysql.connection.commit()
    cur.close()
    
    producto = [{'nombre': nombre, 'descripcion': descripcion, 'precio': precio, 'stock': stock}]
    return jsonify(producto)

@app.route('/agregarpedido/<int:id_empleado>/<string:fecha_pedido>/<int:total>', methods=['POST'])
def agregar_pedido (id_empleado, fecha_pedido, total):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO pedidos (id_empleado, fecha_pedido, total) VALUES (%s, %s, %s)', (id_empleado, fecha_pedido, total))
    mysql.connection.commit()
    cur.close()
    
    pedido = [{'id_empleado': id_empleado, 'fecha_pedido': fecha_pedido, 'total': total}]
    
    return jsonify(pedido)
 
@app.route('/getproducts')
def get_products():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    cur.close()
    products = [{'nombre': row[1], 'descripcion': row[2], 'precio': row[3], 'stock': row[4] } for row in data]
    
        
    return jsonify(products)
 
if (__name__) == '__main__' :
    app.run(port=3000, debug=True)

