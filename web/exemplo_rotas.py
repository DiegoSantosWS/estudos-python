from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Página principal"

@app.route("/clientes")
def clientes():
    return "Página de clientes"

@app.route("/fornecedores")
def fornecedores():
    return "Página de fornecedores"

if __name__ == "__main__":
    app.run()
