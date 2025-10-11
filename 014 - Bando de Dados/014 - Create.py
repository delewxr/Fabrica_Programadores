from db import conexao_banco 

nome = "Rodrgio De Le Martins"
telefone = "11999999999" 
email = "Rodrigoemiguel@icloud.com"
data_nascimento = "2000-01-01" 
senha = "123456"

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