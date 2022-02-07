from flask import Flask
import funcao_cadastrar_chamado as funcao
import consulta_chamado as consulta_status
import finalizar_chamado as finalizar

app = Flask(__name__)

@app.route("/",methods=["GET"])
def documentacao():
    return "Em breve a documentação da API"

@app.route("/ti/<chamado>", methods=["POST"])
def post_chamado(chamado):
    funcao.cadastrar_chamado(chamado)
    return 'ok'
@app.route("/ti/<string:status>",methods=["GET"])
def get_status(status):
    resposta = consulta_status.chamados_status(status)
    resposta = consulta_status.tratar_resposta_multipla(resposta)
    return resposta
@app.route("/ti/fechamento/<chamado_finalizado>",methods=["POST"])
def encerrar_chamando(chamado_finalizado):
    finalizar.encerrar_chamado(chamado_finalizado)
    return "ok"




app.run(host='0.0.0.0')
app.run('localhost',3001,debug=True)