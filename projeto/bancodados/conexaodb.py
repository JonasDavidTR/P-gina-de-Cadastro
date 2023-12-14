import mysql.connector
from mysql.connector import Error

def con():
    try:
        con = mysql.connector.connect(
            host = "localhost",
            passwd = "",
            database = "cadastro",
            user = "root"
        )
    except Error as er:
        print(er)
    finally:
        return con
    
def closedb(con):
    return con.close()
