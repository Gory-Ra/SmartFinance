from database import Session
from models import Transacao
from sqlalchemy import func
from sqlalchemy import extract
from datetime import datetime
import pandas as pd

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

def listar_categorias():
    session = Session()
    # Busca categorias distintas na tabela
    resultado = session.query(Transacao.categoria).distinct().all()
    session.close()
    # Retorna uma lista limpa
    return [c[0] for c in resultado if c[0] is not None]

def gastos_por_categoria():
    session = Session()
    # Busca apenas as despesas e agrupa por categoria somando os valores
    resultados = (
        session.query(Transacao.categoria, func.sum(Transacao.valor))
        .filter(Transacao.tipo == 'Despesa')
        .group_by(Transacao.categoria)
        .all()
    )
    session.close()
    # Retorna um dicionário: {'Alimentação': 500.0, 'Lazer': 200.0}
    return {categoria: total for categoria, total in resultados}

def verificar_alerta_excesso(categoria_alvo, limite_estimado):
    """
    Verifica se o gasto em uma categoria ultrapassou um limite definido.
    """
    gastos = gastos_por_categoria()
    gasto_atual = gastos.get(categoria_alvo, 0)
    
    if gasto_atual > limite_estimado:
        porcentagem_acima = ((gasto_atual - limite_estimado) / limite_estimado) * 100
        return f" Alerta: Gastos com {categoria_alvo} estão {porcentagem_acima:.1f}% acima do esperado!"
    return f" Gastos com {categoria_alvo} dentro do limite."

def deletar_transacao(transacao_id):
    session = Session()
    transacao = session.query(Transacao).filter_by(id=transacao_id).first()
    if transacao:
        session.delete(transacao)
        session.commit()
        print(f" Transação {transacao_id} removida.")
    session.close()

def atualizar_valor_transacao(transacao_id, novo_valor):
    session = Session()
    transacao = session.query(Transacao).filter_by(id=transacao_id).first()
    if transacao:
        transacao.valor = novo_valor
        session.commit()
        print(f" Valor da transação {transacao_id} atualizado para R$ {novo_valor}.")
    session.close()

def total_gasto_no_mes(mes, ano):
    session = Session()
    total = (
        session.query(func.sum(Transacao.valor))
        .filter(Transacao.tipo == 'Despesa')
        .filter(extract('month', Transacao.data) == mes)
        .filter(extract('year', Transacao.data) == ano)
        .scalar() or 0.0 # Retorna 0.0 se não houver gastos
    )
    session.close()
    return total

def exportar_para_csv(caminho_arquivo):
    session = Session()
    transacoes = session.query(Transacao).all()
    
    # Transformando objetos do banco em uma lista de dicionários
    dados = [
        {
            'Data': t.data.strftime('%d/%m/%Y'),
            'Descricao': t.descricao,
            'Valor': t.valor,
            'Tipo': t.tipo,
            'Categoria': t.categoria
        } for t in transacoes
    ]
    
    # Cria um DataFrame e exporta
    df = pd.DataFrame(dados)
    # encoding='utf-8-sig' garante que acentos fiquem certos no Excel
    df.to_csv(caminho_arquivo, index=False, sep=';', encoding='utf-8-sig') 
    
    session.close()