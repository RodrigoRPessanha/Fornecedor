from flask import Flask, render_template, request, jsonify
from database import *

app = Flask(__name__)
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


@app.route('/relatorio', methods=['POST'])
def relatorio():
    filtro = request.form.get('filtro')
    relatorio = selectRelatorioDeProdutos(filtro)
    return render_template('Relatorio/relatorio.html', relatorio=relatorio)


if __name__ == '__main__':
    app.run()
