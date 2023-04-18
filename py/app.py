from flask import Flask, render_template, request, jsonify
from database import *

app = Flask(__name__)

@app.route('/RegistroDeComprasProdutos', methods=['POST'])
def registroDeComprasProdutos():
	nomeProdutos = request.form('nomeProduto')
	qntdProdutos = request.form('quantidadeProdutos')
	preco = request.form('preco')
	fornecedor = request.form('fornecedor')
	insertRegistroDeComprasProdutos(nomeProdutos, qntdProdutos, preco, fornecedor)
	return jsonify({'message': 'Registro realizado com sucesso.'}), 201

@app.route('/registroDeProdutos', methods=['POST'])
def registroDeProdutos():
	nomeProdutos = request.form('nomeProduto')
	qntdProdutos = request.form('quantidadeProdutos')
	preco = request.form('preco')
	fornecedor = request.form('fornecedor')
	insertRegistroDeProdutos(nomeProdutos, qntdProdutos, preco, fornecedor)
	return jsonify({'message': 'Registro realizado com sucesso.'}), 201

@app.route('/relatorio', methods=['GET', 'POST'])
def relatorio():
    filtro = request.form('filtro')
    relatorio = selectRelatorioDeProdutos(filtro)
    return render_template('../html/Relatorio/relatorio.html', relatorio=relatorio)


if __name__ == '__main__':
    app.run()