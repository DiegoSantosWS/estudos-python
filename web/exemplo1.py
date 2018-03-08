from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Página principal"

@app.route("/clientes/<funcao>")
def clientes(funcao):
    if (funcao.lower() == "cadastro"):
        return "Cadastro de clientes"
    elif (funcao.lower() == "consulta"):
        return "Consulta de clientes"
    elif (funcao.lower() == "alterar"):
        return "Alterar de clientes"

if __name__ == "__main__":
    app.run()
