from flask import Flask, request

app = Flask(__name__)

funcionarios = []

@app.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    dados = request.json

    novo_funcionario = {
        "id": len(funcionarios) + 1,
        "nome": dados["nome"],
        "cargo": dados["cargo"],
        "salario": dados["salario"]
    }

    funcionarios.append(novo_funcionario)

    return novo_funcionario, 201

app.run(debug=True)