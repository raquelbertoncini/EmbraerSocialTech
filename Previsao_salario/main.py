from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)


def previsao(lista_valores_formulario):
    prever = np.lista_valores_formulario.values.reshape(-1, 1)
    modelo_salvo = joblib.load('melhor_modelo.sav')  # realiza a carga do modelo salvo
    resultado = modelo_salvo.predict(prever)  # aplica a previsao
    return resultado


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        lista_formulario = request.form.to_dict()  # captura os dados do formulario
        lista_formulario = list(lista_formulario.values())  # transforma os dados em uma lista
        lista_formulario = list(map(float, lista_formulario[1]))  # transforma a lista de string em numeros
        resultado = previsao(lista_formulario)  # aplica a previsao
        # retorna o resultado para uma pagina html
        return render_template("resultado.html", previsao=resultado)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)