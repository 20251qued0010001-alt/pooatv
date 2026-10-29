from flask import Flask, request

app = Flask(__name__)

filmes=[]

@app.route('/filme', methods= ['POST'])
def criar_filme():
    dados= request.json

    novo_filme={
          "id": len(filmes) + 1,
        "nome": dados["nome"],
        "diretor": dados["diretor"],
        "ano": dados["ano"]
    }

    filmes.append(novo_filme)

    return novo_filme, 201
app.run(debug=True)