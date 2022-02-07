import sqlite3
from datetime import  datetime


BANCO = "banco.db"

def cadastrar_chamado(chamado):
    data = datetime.now()
    dataabertura = data.strftime('%d/%m/%Y %H:%M')
    status = "aberto"

    j = eval(chamado)
    user = j["user"]
    cliente = j["cliente"]
    contato = j["contato"]
    relato = j["relato"]


    conexao = sqlite3.connect(BANCO)
    c = conexao.cursor()
    c.execute("SELECT * FROM chamado ")
    c.execute("INSERT INTO chamado(user,cliente,contato,dataabertura,relato,status) values (?,?,?,?,?,?)",(user,cliente,contato,dataabertura,relato,status))
    conexao.commit()
    conexao.close()
    print("Sucesso ao cadastrar chamado")