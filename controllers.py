from flask import render_template, request
from pprint import pprint
from app import app

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/formulario', methods=['POST'])
def confirm():
    print('processando requisição POST')
    pprint(request.form)
    email = request.form.get('email')
    senha = request.form.get('senha')

    dados = {
        'email': email,
        'senha': senha
    }

    return render_template('index.html', **dados)