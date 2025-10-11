import mysql.connector

def conexao_banco():#
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="aula"
)
    return conexao

