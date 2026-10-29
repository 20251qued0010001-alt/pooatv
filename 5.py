from flask import Flask, request

app = Flask(__name__)

produtos = []

@app.route('/Produtos', methods=['POST'])
def criar_produto():
    dados = request.json

    novo_produto = {
        "id": len(produtos) + 1,
        "nome": dados["nome"],
        "preco": dados["preco"],
        "categoria": dados["categoria"]
    }

    produtos.append(novo_produto)

    return novo_produto, 201

app.run(debug=True)