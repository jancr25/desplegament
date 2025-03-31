from flask import Flask, jsonify
import mysql.connector
import os

dbconfig = {
    'host': 'localhost',
    'database': 'comptador',
    'user': 'flaskuser',
    'password': 'password'
}

pool_name = "mysql_pool"
pool_size = 3

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = pool_name,
                                                      pool_size = pool_size,
                                                      **dbconfig)

app = Flask(__name__)

def get_db_connection():
    return cnxpool.get_connection()

@app.route('/')
def incrementar():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE visites SET comptador = comptador + 1 WHERE id = 1')
    conn.commit()
    cursor.close()
    conn.close()
    return "Visita afegida!"

@app.route('/comptador')
def valor_actual():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT comptador FROM visites WHERE id = 1')
    comptador = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return jsonify(comptador=comptador)

if __name__ == '__main__':
    port = os.getenv('PORT') if os.getenv('PORT') else 5000
    app.run(host='0.0.0.0', port=port)
