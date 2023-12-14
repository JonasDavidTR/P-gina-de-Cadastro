from __init__ import app
from flask import render_template, request, jsonify


@app.route('/index', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        #dados_usuario = request.get_json()
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirmarSenha = request.form.get('confirmarSenha')

       
        if senha == confirmarSenha:
            mensagem = "Cadastro realizado com sucesso!"
            return render_template('index.html', mensagem=mensagem)
            #Inserir dados no banco de dados
        else:
            mensagem = "A senhas não coincidem. Por favor, tente novamente!"
            return render_template('index.html', mensagem=mensagem)

    return render_template('index.html')

app.run(debug=True)
