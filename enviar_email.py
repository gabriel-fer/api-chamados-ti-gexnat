from ast import stmt
import smtpd
import smtplib
import email.message
from datetime import datetime
from senha import senha

def enviar_email(chamado):
    data = datetime.now()
    dataabertura = data.strftime('%d/%m/%Y %H:%M')
    j = eval(chamado)
    user = j["user"]
    cliente = j["cliente"]
    contato = j["contato"]
    relato = j["relato"]


    corpo =f"""
    <p>Prezados,</p>
    <p>Um novo chamado foi aberto:</p>
    <p>Quem abriu:{user}</p>
    <p>Para quem é o chamado:{cliente}</p>
    <p>telefone para contato: {contato}</p>
    <p>data de abertura do chamado:{dataabertura}</p>
    <p>Relato: {relato}</p>

    
    """
    
    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = ''
    msg['to'] = ''
    senha_email = senha
    msg.add_header('Content-Type','text/html')
    msg.set_payload(corpo)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()

    s.login(msg['From'],senha_email)
    s.sendmail(msg['From'],[msg['to']],msg.as_string().encode('utf-8'))
    print("email enviado")
