import sqlite3

def conectar():
    conn = sqlite3.connect('registros.db')
    return conn

def createTableRegistroDeComprasProdutos():
    conn = conectar()
    conn.execute('''CREATE TABLE IF NOT EXISTS 	REGISTRO_DE_COMPRAS_PRODUTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        NOME_PRODUTO TEXT NOT NULL, 
        QNTD_PRODUTOS INTEGER NOT NULL, 
        PRECO DECIMAL(11, 2) NOT NULL, 
        NOME_FORNECEDOR TEXT NOT NULL);''')
    conn.close()

def createTableRegistroDeProdutos():
    conn = conectar()
    conn.execute('''CREATE TABLE IF NOT EXISTS 	REGISTRO_DE_PRODUTOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        NOME_PRODUTO TEXT NOT NULL, 
        QNTD_PRODUTOS INTEGER NOT NULL, 
        PRECO DECIMAL(11, 2) NOT NULL, 
        NOME_FORNECEDOR TEXT NOT NULL);''')
    conn.close()

def insertRegistroDeComprasProdutos(nomeProdutos, qntdProdutos, preco, nomeFornecedor):
    conn = conectar()
    conn.execute("INSERT INTO REGISTRO_DE_COMPRAS_PRODUTOS(NOME_PRODUTO, QNTD_PRODUTOS, PRECO, NOME_FORNECEDOR)\
        VALUES (?, ?, ?, ?)", (nomeProdutos, qntdProdutos, preco, nomeFornecedor))
    conn.commit()
    conn.close()

def insertRegistroDeProdutos(nomeProdutos, qntdProdutos, preco, nomeFornecedor):
    conn = conectar()
    conn.execute("INSERT INTO REGISTRO_DE_PRODUTOS(NOME_PRODUTO, QNTD_PRODUTOS, PRECO, NOME_FORNECEDOR)\
        VALUES (?, ?, ?, ?)", (nomeProdutos, qntdProdutos, preco, nomeFornecedor))
    conn.commit()
    conn.close()

def deletarRegistroDeComprasProdutos(id : int):
    conn = conectar()
    if id:
        conn.execute(f"DELETE FROM REGISTRO_DE_COMPRAS_PRODUTOS WHERE ID = {id}")

def deletarRegistroDeProdutos(id : int):
    conn = conectar()
    if id:
        conn.execute(f"DELETE FROM REGISTRO_DE_PRODUTOS WHERE ID = {id}")

def selectRelatorioDeProdutos(id : int):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT NOME_PRODUTO, QNTD_PRODUTOS, PRECO, NOME_FORNECEDOR FROM REGISTRO_DE_PRODUTOS WHERE ID = {id};")
    relatorio = cursor.fetchall()
    registro = lista(relatorio)
    cursor.close()
    conn.close()
    return registro

def lista(resultados: list):
    registros = []
    for linha in resultados:
        registro = {}
        registro['nomeProduto'] = linha[0]
        registro['qntdProdutos'] = linha[1]
        registro['preco'] = linha[2]
        registro['fornecedor'] = linha[3]
        registros.append(registro)
    return registros
