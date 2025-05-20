from flask import Flask

app = Flask(__name__)

@app.route("/username/<nome>/1")
def cumprimento(nome):
    return f"<h1>Olá, {nome}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)