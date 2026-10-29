from flask import Flask, request

app = Flask(__name__)

cidades = []

@app.route('/cidades', methods=['POST'])
def criar_cidade():
    dados = request.json

    nova_cidade = {
        "id": len(cidades) + 1,
        "nome": dados["nome"],
        "preco": dados["preco"],
        "categoria": dados["categoria"]
    }

    cidades.append(nova_cidade)

    return nova_cidade, 201

app.run(debug=True)