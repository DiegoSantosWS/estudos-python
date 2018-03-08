from flask import Flask
app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'Olá, Mundo!'

@app.route('/teste')
def ola_teste():
    return 'Você solicitou teste.'