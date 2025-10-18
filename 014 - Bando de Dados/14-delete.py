from db import conexao_banco #estabelece a conexão com o banco de dados 

conexao = conexao_banco() # cria a conexão com o banco de dados
# verifica se a conexão foi bem sucedida
if conexao.is_connected():
    cursor = conexao.cursor()
# solicita o ID do cliente a ser atualizado
    user_name = input("Digite o nome do cliente que deseja deletar: ")
    sql = "DELETE FROM cliente WHERE nome = %s"
    dados = (user_name, )

    cursor.execute(sql, dados)
    conexao.commit()

    cursor.close()
    conexao.close()
else:
    print("Não foi possível conectar ao banco de dados.")
    exit()