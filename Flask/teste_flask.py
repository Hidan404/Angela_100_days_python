from flask import Flask, request, jsonify


app = Flask(__name__)

def negrito(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if isinstance(response, str):
            return f"<strong>{response}</strong>"
        return response
    return wrapper

def sublinhado(funcao):
    def wrapper(*args, **kwargs):
        resposta = funcao(*args, **kwargs)
        if isinstance(resposta, str):
            return f"<u>{resposta}</u>"
        return resposta
    return wrapper

def emfase(funcao):
    def wrapper(*args, **kwargs):
        resposta = funcao(*args, **kwargs)
        if isinstance(resposta, str):
            return f"<em>{resposta}</em>"
        return resposta
    return wrapper

@app.route("/")
@negrito
@sublinhado
@emfase
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/bye")
def goodbye_world():
    return "<h1>Goodbye, World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)