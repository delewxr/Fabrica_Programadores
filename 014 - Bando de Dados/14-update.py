from db import conexao_banco #estabelece a conexão com o banco de dados 

conexao = conexao_banco() # cria a conexão com o banco de dados
# verifica se a conexão foi bem sucedida
if conexao.is_connected():
    cursor = conexao.cursor()

# solicita o ID do cliente a ser atualizado
    user_id = input("Digite o ID do cliente que deseja atualizar: ")
    novo_nome = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo telefone: ")
    novo_email = input("Digite o novo e-mail: ")
    nova_data_nascimento = input("Digite a nova data de nascimento (YYYY-MM-DD): ")
    nova_senha = input("Digite a nova senha: ") 
    sql = """
        UPDATE cliente
        SET nome = %s,'     
        telefone = %s,
        email = %s,
        data_nascimento = %s,
        senha = %s
        WHERE id = %s
    """
    #Tupla com os novos dados e o ID do cliente na mesma ordem dos placeholders() na query SQL
    dados = (novo_nome, novo_telefone, novo_email, nova_data_nascimento, nova_senha, user_id)



    cursor.execute(sql, dados)
    conexao.commit()

    cursor.close()
    conexao.close()
else:
    print("Não foi possível conectar ao banco de dados.")
    exit()