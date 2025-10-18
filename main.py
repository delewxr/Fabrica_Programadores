from flask import Flask #importa somente o modulo Flask
from routes import clientes #importa o blueprint 'clientes' do arquivo routes.py
app = Flask(__name__) # é uma variavel que inicia nossa aplicação 

app.register_blueprint(clientes) #registra o blueprint 'clientes' na aplicação Flask

if __name__ == "__main__":
    app.run(debug=True)
