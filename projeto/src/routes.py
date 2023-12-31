from __init__ import app
from Bancodados import db, conexaodb
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            # Dados google
            dados_usuarios = request.json()
            nome = dados_usuarios.get('nome')
            senha = dados_usuarios.get('senha')
            email = dados_usuarios.get('email')
            print(nome)
        else:
            # Dados formulário
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = request.form.get('senha')
            confirmarSenha = request.form.get('confirmarSenha')


        if nome == " " or nome == None:
            mensagem = "Nome de usuário inválido. Tente novamente!"
            return render_template('index.html', mensagem=mensagem)


        if senha == confirmarSenha:
            if conexaodb.con() == None:
                mensagem = "Erro de Conexão, Verifique sua conexão ou tente novamente mais tarde!"
                return render_template('index.html', mensagem=mensagem)
            else:
                db.insert(nome, email, senha)
                mensagem = "Cadastro realizado com sucesso!"
                return render_template('index.html', mensagem=mensagem)
        else:
            mensagem = "A senhas não coincidem. Por favor, tente novamente!"
            return render_template('index.html', mensagem=mensagem)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,  host='localhost', port=5000)
