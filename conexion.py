from mysql import connector
import mysql

host = "213.171.200.101"
user = "carlos"
password = "Admin12345"
db = "inventario"

conexion = mysql.connector.connect(host=host, user=user, passwd=password, db=db)
cursor = conexion.cursor()


def desconectar():
    conexion.close()
    conexion.close()

