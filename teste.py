import sqlite3
from datetime import  datetime
BANCO = "banco.db"



data = datetime.now()
datafechamento = data.strftime('%d/%m/%Y %H:%M')
status = "fechado"
id = 1
fechamento = "o chamado foi finalizado"

conexao = sqlite3.connect(BANCO)
c = conexao.cursor()
c.execute("UPDATE chamado SET datafechamento = ?, status = ?, fechamento = ?  WHERE id = ?", (datafechamento, status, fechamento, id))
conexao.commit()
conexao.close()
print("Sucesso ao encerrar o chamado")