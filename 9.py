app = Flask(__name__)

restaurantes = []

@app.route('/restaurantes', methods=['POST'])
def criar_restaurante():
    dados = request.json

    novo_restaurante = {
        "id": len(restaurantes) + 1,
        "nome": dados["nome"],
        "tipo": dados["tipo"],
        "cidade": dados["cidade"]
    }

    restaurantes.append(novo_restaurante)

    return novo_restaurante, 201

app.run(debug=True)