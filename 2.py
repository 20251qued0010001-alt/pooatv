from flask import Flask, request

app = Flask(__name__)

alunos = []

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.json

    novo_aluno = {
        "id": len(alunos) + 1,
        "nome": dados["nome"],
        "curso": dados["curso"],
        "idade": dados["idade"]
    }

    alunos.append(novo_aluno)

    return novo_aluno, 201

app.run(debug=True)