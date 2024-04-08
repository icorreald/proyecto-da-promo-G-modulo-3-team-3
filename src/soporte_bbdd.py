import mysql.connector

def creacion_bbdd(query, contrasenia, nombre_bbdd=None):
    if nombre_bbdd is not None:
        cnx = mysql.connector.connect(
            user = 'root',
            password = contrasenia,
            host = '127.0.0.1')
        
        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)

        except mysql.connector.connect.Error as err:
            print(err)
            print('Error code', err.errno)
            print('SQLSTATE', err.sqlstate)
            print('Message', err.msg)
        
    else:
        cnx = mysql.connector.connect(
            user = 'root',
            password = contrasenia,
            host = '127.0.0.1',
            database = nombre_bbdd)

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)

        except mysql.connector.connect.Error as err:
            print(err)
            print('Error code', err.errno)
            print('SQLSTATE', err.sqlstate)
            print('Message', err.msg)