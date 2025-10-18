from flask import render_template, render_template, request #usado para renderizar as templetes de HTML
from db import conexao_banco #importa a função que estabelece a conexão com o banco de dados

clientes = Blueprint('clientes', __name__) #cria um blueprint chamado 'clientes'

@clientes.route('/', methods=['GET', 'POST']) #define a rota '/' que aceita métodos GET e POST
def cadastrar_cliente():
    if request.method == 'POST': #verifica se o método da requisição é POST
        nome = request.form['nome'] #obtém o valor do campo 'nome' do formulário
        telefone = request.form['telefone'] #obtém o valor do campo 'telefone' do formulário
        email = request.form['email'] #obtém o valor do campo 'email' do formulário
        data_nascimento = request.form['data_nascimento'] #obtém o valor do campo 'data_nascimento' do formulário
        senha = request.form['senha'] #obtém o valor do campo 'senha' do formulário
        conexao= conexao_banco() #cria a conexão com o banco de dados
        if conexao.is_connected(): #verifica se a conexão foi bem sucedida
            cursor = conexao.cursor() #cria um cursor para executar comandos SQL

        sql = """
            INSERT INTO cliente (nome, telefone, email, data_nascimento, senha)
            VALUES (%s, %s, %s, %s, %s)
        """ #comando SQL para inserir um novo cliente na tabela 'cliente'
        
        dados = (nome, telefone, email, data_nascimento, senha) #tupla com os dados a serem inseridos

        cursor.execute(sql, dados) #executa o comando SQL com os dados fornecidos
        conexao.commit() #confirma a transação no banco de dados

        cursor.close() #fecha o cursor
        conexao.close() #fecha a conexão com o banco de dados
        return "Cliente cadastrado com sucesso!" #retorna uma mensagem de sucesso
    else:
        print("Não foi possível conectar ao banco de dados.")