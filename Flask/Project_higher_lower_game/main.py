from flask import Flask

app = Flask(__name__)

@app.route("/username/<nome>/1")
def cumprimento(nome):
    return f"<h1 style='color: blue;'>Olá, {nome}!</h1>"\
           f"<h2 style='color: green;'>Bem-vindo ao nosso site!</h2>"\
           f"<p style='color: purple;'>Estamos felizes em tê-lo aqui.</p>"\
           f"<p style='color: orange;'>Divirta-se navegando!</p>"\
           f"<img src='https://media.giphy.com/media/3o7aD2sa1v4x5q0g8I/giphy.gif' alt='giphy' width='300' height='200'></img>"

if __name__ == "__main__":
    app.run(debug=True)