from flask import Flask, request

app = Flask(__name__)

jogos = []

@app.route('/jogos', methods=['POST'])
def criar_jogo():
    dados = request.json

    novo_jogo = {
        "id": len(jogos) + 1,
        "nome": dados["nome"],
        "genero": dados["genero"],
        "ano": dados["ano"]
    }

    jogos.append(novo_jogo)

    return novo_jogo, 201

app.run(debug=True)