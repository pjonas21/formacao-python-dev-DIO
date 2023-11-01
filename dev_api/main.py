from flask import Flask, jsonify, request
import json

app = Flask(__name__)

lista = [
    {"nome": "Paulo",
     "habilidadedes": [
         "Python", "Java", "Django"
     ]
     },
    {"nome": "Jonas",
     "habilidadedes": [
         "Python", "JavaScript", "Angular"
     ]
     }
]


@app.route("/dev/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = lista[id]
        except IndexError:
            response = {"status":"erro", "mensagem":"Desenvolvedor nao existe"}
        except Exception:
            response = {"status":"erro", "mensagem":"Procure o administrador da API"}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        lista[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        lista.pop(id)
        return jsonify({"status": "sucesso", "mensagem": "Registro excluido."})


@app.route("/dev/", methods=['GET', 'POST'])
def listar_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        lista.append(dados)
        return jsonify({"status":"sucesso", "mensagem":"Desevolvedor inserido com sucesso"})
    elif request.method == 'GET':
        return jsonify({'lista': lista})


if __name__ == '__main__':
    app.run(debug=True)
