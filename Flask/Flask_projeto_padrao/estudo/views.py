from flask import  render_template, request, url_for
from estudo import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]
        
        # Aqui você pode adicionar lógica para processar os dados recebidos
        # Por exemplo, salvar em um banco de dados ou enviar um e-mail
        
        return render_template("index.html", nome=nome, idade=idade, email=email, mensagem=mensagem)
    
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")