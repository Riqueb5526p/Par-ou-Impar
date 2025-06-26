from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        try:
            numero = int(request.form["numero"])
            if numero == 0:
                resultado = "Encerrando..."
            elif numero % 2 == 0:
                resultado = f"O número {numero} é par."
            else:
                resultado = f"O número {numero} é ímpar."
        except ValueError:
            resultado = "Digite um número válido!"
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
