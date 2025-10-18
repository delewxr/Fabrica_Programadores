from db import conexao_banco 

nome = input("Digite o nome do cliente: ")
telefone = input("Digite o telefone do cliente: ")
email = input("Digite o e-mail do cliente: ")
data_nascimento =  input("Digite a data de nascimento do cliente (YYYY-MM-DD): ")
senha = input("Digite a senha do cliente: ")

conexao = conexao_banco()

if conexao.is_connected():
    cursor = conexao.cursor()

    sql = '''
    INSERT INTO cliente (nome, telefone, email, data_nascimento, senha) 
    VALUES (%s, %s, %s, %s, %s)
    '''

    dados = (nome, telefone, email, data_nascimento, senha)

    cursor.execute(sql, dados)
    conexao.commit()

    cursor.close()
    conexao.close()
else:
    print("Erro ao conectar ao banco de dados")