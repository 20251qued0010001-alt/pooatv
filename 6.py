from flask import Flask, request

app = Flask(__name__)

carros = []

@app.route('/carros', methods=['POST'])
def criar_carro():
    dados = request.json

    novo_carro = {
        "id": len(carros) + 1,
        "modelo": dados["modelo"],
        "marca": dados["marca"],
        "ano": dados["ano"]
    }

    carros.append(novo_carro)

    return novo_carro, 201

app.run(debug=True)












                     