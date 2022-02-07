import sqlite3
from datetime import  datetime
BANCO = "banco.db"


def encerrar_chamado(chamado_finalizado):
    data = datetime.now()
    datafechamento = data.strftime('%d/%m/%Y %H:%M')
    status = "fechado"
    j = eval(chamado_finalizado)
    id = j['id']
    fechamento = j['fechamento']

    conexao = sqlite3.connect(BANCO)
    c = conexao.cursor()
    c.execute("""
    UPDATE chamado
    SET datafechamento = ?, status = ?, fechamento = ? 
    WHERE id = ?
    """,(datafechamento,status,fechamento,id))
    conexao.commit()
    conexao.close()
    print("Sucesso ao encerrar o chamado")



