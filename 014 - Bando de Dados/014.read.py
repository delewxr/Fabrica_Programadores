from db import conexao_banco 

conexao = conexao_banco()
#
if conexao.is_connected():
    cursor = conexao.cursor() 

    nome_consulta = input("Digite o nome que deseja consultar: ")

    sql = "SELECT id, nome, telefone, email, data_nascimento,senha FROM cliente where nome = %s"
    cursor.execute(sql, (nome_consulta,))

    cliente = cursor.fetchone()

    if cliente:
    
            print(f"ID: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"Telefone: {cliente[2]}")
            print(f"E-mail: {cliente[3]}")
            print(f"Data de Nascimento: {cliente[4]}")
            print(f"Senha: {cliente[5]}")
            print("-" * 20)
    else:
            print("Nenhum cliente encontrado com esse nome.")