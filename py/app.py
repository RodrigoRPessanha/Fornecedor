from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from database import *

app = Flask(__name__)
CORS(app)
app.debug = True


@app.route('/registroDeComprasProdutos', methods=['POST'])
def registroDeComprasProdutos():
    nomeProdutos = request.form['nomeProduto']
    qntdProdutos = request.form['quantidadeDeProdutos']
    preco = request.form['preco']
    fornecedor = request.form['fornecedor']
    insertRegistroDeComprasProdutos(
        nomeProdutos, qntdProdutos, preco, fornecedor)
    return jsonify({'message': 'Registro realizado com sucesso.'}), 201


@app.route('/registroDeProdutos', methods=['POST'])
def registroDeProdutos():
    nomeProdutos = request.form['nomeProduto']
    qntdProdutos = request.form['quantidadeDeProdutos']
    preco = request.form['preco']
    fornecedor = request.form['fornecedor']
    insertRegistroDeProdutos(nomeProdutos, qntdProdutos, preco, fornecedor)
    return jsonify({'message': 'Registro realizado com sucesso.'}), 201


@app.route('/relatorio', methods=['GET'])
def relatorio():
    filtro = request.args.get('filtro')
    relatorio = selectRelatorioDeProdutos(filtro)
    print(request.method, '//', request.args, '//',
          request.form, '//', filtro, '//', request.args.get('filtro'))
    print(relatorio)
    return jsonify(relatorio)
    # return render_template('Relatorio/relatorio.html', relatorio=relatorio)


if __name__ == '__main__':
    app.run()
