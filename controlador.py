from conexion import cursor, conexion, desconectar

def add_product(name, price, quantity):
    sql = "INSERT INTO Productos (nombre, precio, cantidad) VALUES(%s, %s, %s)"
    cursor.execute(sql, (name, price, quantity))
    conexion.commit()


def search_products(items):
    sql = "SELECT * FROM Productos WHERE id = %s or LOWER(nombre) LIKE LOWER(%s)"
    cursor.execute(sql, (items, "%" + items + "%"))
    result = cursor.fetchall()
    return result


def get_products():
    sql = "SELECT * FROM Productos"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def update_product(id, name, price, quantity):
    sql = "UPDATE Productos SET nombre = %s, precio = %s, cantidad = %s WHERE id = %s"
    cursor.execute(sql, (name, price, quantity, id))
    conexion.commit()


def update_stock(id, quantity):
    sql = "UPDATE Productos SET cantidad = %s WHERE id = %s"
    cursor.execute(sql, (quantity, id))
    conexion.commit()


def delete_product(id):
    sql = "DELETE FROM Productos WHERE id = %s"
    cursor.execute(sql, (id, ))
    conexion.commit()

# transacciones table
def insert_invoice(total, subtotal, iva, id_cliente):
    sql = "INSERT INTO Factura (total, subtotal, iva, fk_cliente) VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, (total, subtotal, iva, id_cliente))
    conexion.commit()
    return cursor.lastrowid


def insert_record(quantity, total, invoice_id, producto_id):
    sql = "INSERT INTO Registro (cantidad, total, fk_factura,fk_producto) VALUES(%s, %s, %s, %s)"
    cursor.execute(sql, (quantity, total, invoice_id, producto_id))
    conexion.commit()


def get_transactions():
    sql = "SELECT * FROM Transacciones"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def update_transactions(id, quantity, total):
    sql = "UPDATE Transacciones SET cantidad = %s total = %s WHERE id = %s"
    cursor.execute(sql, (quantity, total, id))
    conexion.commit()


def search_product_id(id):
    sql = "SELECT * FROM Productos WHERE id = %s"
    cursor.execute(sql, (id, ))
    result = cursor.fetchone()
    return result


# def actualizar_producto(id, nombre, precio, cantidad):
#     sql = "UPDATE Productos SET nombre = %s, precio = %s, cantidad = %s WHERE id = %s"
#     cursor.execute(sql, (nombre, precio, cantidad, id))
#     conexion.commit()


def get_invoice(id):
    sql = "SELECT * FROM Factura WHERE id = %s"
    cursor.execute(sql, (id, ))
    result = cursor.fetchone()
    return result


def get_invoice_records(invoice_id):
    sql = """SELECT P.id, P.nombre, P.precio, R.cantidad, R.total
     FROM (Factura F JOIN Registro R on F.id = R.fk_factura) 
     JOIN Productos P on R.fk_producto = P.id WHERE F.id = %s"""
    cursor.execute(sql, (invoice_id, ))
    result = cursor.fetchall()
    return result


def get_date_records(start_date, end_date):
    sql = """SELECT P.id, P. nombre, P.precio, sum(R.cantidad) as cantidad_vendida, round(sum(R.total), 2) as total_ventas
    FROM (Factura F JOIN Registro R on F.id = R.fk_factura) JOIN Productos P on R.fk_producto = P.id
    WHERE F.fecha BETWEEN %s AND %s group by(P.id)"""

    cursor.execute(sql, (start_date, end_date))
    result = cursor.fetchall()
    return result


def get_products_quantity():
    sql = """SELECT * FROM  Productos WHERE cantidad <= 15"""
    cursor.execute(sql, ())
    result = cursor.fetchall()
    return result


def validate_user(user, password):
    sql = """SELECT * FROM  administrador WHERE username = %s AND password = %s LIMIT 1"""
    cursor.execute(sql, (user, password))
    result = cursor.fetchone()
    return result


def search_client(document):
    sql = """SELECT * FROM  cliente WHERE cedula = %s LIMIT 1"""
    cursor.execute(sql, (document,))
    result = cursor.fetchone()
    return result


def search_client_id(id_client):
    sql = """SELECT * FROM  cliente WHERE id_cliente = %s LIMIT 1"""
    cursor.execute(sql, (id_client,))
    result = cursor.fetchone()
    return result


def insert_client(firts_name, last_name, document, phone, address):
    sql = "INSERT INTO cliente (nombre, apellido, cedula , telefono, direccion) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(sql, (firts_name, last_name, document, phone, address))
    conexion.commit()
    return cursor.lastrowid


def update_password(newPassword):
    sql = "UPDATE administrador SET password = %s WHERE id = 1"
    cursor.execute(sql, (newPassword,))
    conexion.commit()



