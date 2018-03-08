from flask import Flask # Primeiro importamos a Classe Flask
app = Flask(__name__) # Criamos uma instância da classe Flask chamada app
                      # O argumento é o nome do módulo ou pacote do
                      # aplicativo (__name__)
@app.route('/')       # Definição da URL que executará a função abaixo
def hello_world():    # Função que retorna uma frase exibida no navegador
    return 'Hello, World!'