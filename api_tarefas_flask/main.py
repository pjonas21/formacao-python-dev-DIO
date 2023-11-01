import json

from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 0, "responsavel": "Paulo", "tarefa": "tarefa 1", "status": False},
    {"id": 1, "responsavel": "Jonas", "tarefa": "tarefa 2", "status": False},
]


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify({"tarefas": tarefas})


@app.route("/tarefa", methods=["POST"])
def adicionar_tarefa():
    dados = json.loads(request.data)
    indice = len(tarefas)
    if not dados:
        return jsonify({"status": "erro", "mensagem": "Dados incorretos."})
    else:
        dados["id"] = indice
        tarefas.append(dados)
        return jsonify(dados)


@app.route("/tarefa/<int:id>", methods=["GET"])
def buscar_tarefa(id):
    try:
        response = tarefas[id]
    except IndexError:
        mensagem = "Nao ha tarefa com o ID solicitado."
        return jsonify({"status": "erro", "mensagem": mensagem})

    return jsonify({"tarefa": response})


@app.route("/tarefa/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    try:
        tarefa = tarefas[id]
    except IndexError:
        mensagem = "Nao ha tarefa com o ID solicitado."
        return jsonify({"status": "erro", "mensagem": mensagem})

    novo_status = json.loads(request.data)

    try:
        status_atualizado = novo_status["status"]
    except KeyError:
        mensagem = "Edicao nao permitida."
        return jsonify({"status": "erro", "mensagem": mensagem})

    tarefa["status"] = status_atualizado
    return jsonify({"tarefa atualizada": tarefa})


@app.route("/tarefa/<int:id>", methods=["DELETE"])
def excluir_tarefa(id):
    try:
        tarefas[id]
    except IndexError:
        mensagem = "Nao ha tarefa com o ID solicitado."
        return jsonify({"status": "erro", "mensagem": mensagem})
    except Exception:
        mensagem = "Erro inesperado. Contacte o administrador."
        return jsonify({"status": "erro", "mensagem": mensagem})

    tarefas.pop(id)
    return jsonify({"status": "sucesso", "mensagem": "Tarefa excluida."})


if __name__ == '__main__':
    app.run(debug=True)
