from Bancodados.conexaodb import con, closedb
from mysql.connector import Error

def insert(nome, email, senha):

    vcon = con()
    cursor = vcon.cursor()
    try:
        sql = "INSERT INTO `users` VALUE (null, %s, %s, %s);"
        values = (nome, email, senha)
        cursor.execute(sql, values)
        vcon.commit()

    except Error as er:
        print("Falha na insersão de dados", er)
        raise
    finally:
        if cursor:
            closedb(cursor)
        if vcon:
            closedb(vcon)
