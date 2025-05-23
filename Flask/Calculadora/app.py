from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculadora():
    if request.method == "POST":
        numero1 = float(request.form["numero1"])
        numero2 = float(request.form["numero2"])
        operacao = request.form["operacao"]

        if operacao == "soma":
            resultado = numero1 + numero2
        elif operacao == "subtracao":
            resultado = numero1 - numero2
        elif operacao == "multiplicacao":
            resultado = numero1 * numero2
        elif operacao == "divisao":
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                resultado = "Erro: Divisão por zero"
        else:
            resultado = "Operação inválida"
        
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)