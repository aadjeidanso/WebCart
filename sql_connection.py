import mysql.connector

__cnx = None

#This will be the authentication of the SQL connection between our server and db
def get_sql_connection():
    global __cnx 
    if __cnx is None:
        __cnx = mysql.connector.connect(
        user='root',
        password='cHRISTcON@#1722',
        host='127.0.0.1',
        database='christdia',
        auth_plugin='mysql_native_password'
)
    return __cnx
