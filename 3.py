from flask import Flask, request

app = Flask(__name__)

musicas = []

@app.route('/musicas', methods=['POST'])
def criar_musica():
    dados = request.json

    nova_musica = {
        "id": len(musicas) + 1,
        "nome": dados["nome"],
        "artista": dados["artista"],
        "ano": dados["ano"]
    }

    musicas.append(nova_musica)

    return nova_musica, 201
app.run(debug=True)