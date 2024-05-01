import mysql.connector
from mysql.connector import Error, cursor
from dotenv import load_dotenv
import os

load_dotenv()

userDB = os.environ.get('userDB')
passwdDB = os.environ.get('passwdDB')

def con():
    con = None
    try:
        con = mysql.connector.connect(
            host = "localhost",
            passwd = passwdDB,
            database = "cadastro",
            user = userDB
        )
        return con
    except Error as er:
        print("Erro de conexao com o banco de dados")
        return None



def closedb(con):
    return con.close()
