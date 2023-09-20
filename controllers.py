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
    name = request.form.get('nome')
    telefone = request.form.get('telefone')
    accept_whatsapp = request.form.get('accept-whatsapp')
    print('checkbox whatsapp', accept_whatsapp)

    dados = {
        'name': name,
        'telefone': telefone,
        'accept_whatsapp': accept_whatsapp
    }

    return render_template('index.html', **dados)