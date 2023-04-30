#Objetivo
#URL base:
#Endpoint: 
#- localhost/contas (GET)
##- localhost/contas (POST)
#- localhost/contas/id (GET)
#- localhost/contas/id (PUT)
#- localhost/contas/id (DELETE)

#quais recursos: CONTAS


#Disponibiliza consulta, criação, exclusão de usuário

from flask import Flask, jsonify, request

app = Flask(__name__)

contas = [
    {
        'id':1,
        'nome':'Wander',
        'login':'wanderasb41',
        'senha':'2020002866',
    }
]

#Consultar por id
#Cosultar todos


@app.route('/contas', methods=['GET'])
def obter_conta():
    return jsonify(contas)

@app.route('/contas/<int:id>', methods=['GET'])
def obter_conta_id(id):
    for conta in contas:
        if conta.get('id') == id:
            return jsonify(conta)

@app.route('/contas/<int:id>', methods=['PUT'])
def editar(id):
    conta_alterada = request.get_json()
    for conta in contas:
        if conta.get('id') == id:
            conta.update(conta_alterada)
            return jsonify(conta)
    return jsonify({'erro': 'Conta não encontrada'})


@app.route('/contas', methods=['POST'])
def criar_conta():
    nova_conta = request.get_json()
    contas.append(nova_conta)
    return jsonify(contas)

@app.route('/contas/<int:id>', methods=['DELETE'])
def excluir_conta(id):
    for conta in contas:
        if conta.get('id') == id:
            contas.remove(conta)
            break

    return jsonify(contas)

app.run(port=5000, host='localhost', debug=True)