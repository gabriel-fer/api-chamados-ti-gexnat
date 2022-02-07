import sqlite3
from flask import jsonify
BANCO = "banco.db"
registro_db = ['id', 'user', 'cliente', 'contato', 'data', 'relato','status']

def chamados_status(status):

    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    c = conexao.cursor()
    c.execute("select * from chamado where status like ?", (status,))
    resposta = c.fetchall()
    return resposta

def tratar_resposta_multipla(resposta):
    lista_resposta_tratada = []
    for registro in resposta:
        lista_resposta_tratada.append(dict(registro))
    return jsonify(lista_resposta_tratada)
