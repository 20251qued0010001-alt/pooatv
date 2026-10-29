from flask import Flask, request

app = Flask(__name__)

cursos = []

@app.route('/cursos', methods=['POST'])
def criar_curso():
    dados = request.json

    novo_curso = {
        "id": len(cursos) + 1,
        "nome": dados["nome"],
        "instituicao": dados["instituicao"],
        "duracao": dados["duracao"]
    }

    cursos.append(novo_curso)

    return novo_curso, 201

app.run(debug=True)