from database import Session
from models import Transacao

def adicionar_transacao(descricao, valor, tipo, categoria):
    session = Session()
    nova_transacao = Transacao(
        descricao=descricao, 
        valor=valor, 
        tipo=tipo, 
        categoria=categoria
    )
    session.add(nova_transacao)
    session.commit()
    session.close()

def listar_transacoes():
    session = Session()
    transacoes = session.query(Transacao).all()
    session.close()
    return transacoes

def calcular_saldo():
    session = Session()
    transacoes = session.query(Transacao).all()
    
    receitas = sum(t.valor for t in transacoes if t.tipo == 'Receita')
    despesas = sum(t.valor for t in transacoes if t.tipo == 'Despesa')
    
    session.close()
    return receitas - despesas