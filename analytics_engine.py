from sqlalchemy import func, extract
from database import Session
from models import Transacao
from datetime import datetime

def calcular_media_historica(categoria):
    """Calcula a média de gastos dos últimos 3 meses para uma categoria."""
    session = Session()
    
    # Busca a soma dos gastos por mês para a categoria nos últimos 3 meses
    resultados = (
        session.query(func.sum(Transacao.valor))
        .filter(Transacao.categoria == categoria)
        .filter(Transacao.tipo == 'Despesa')
        .group_by(extract('month', Transacao.data))
        .limit(3)
        .all()
    )
    session.close()
    
    valores = [r[0] for r in resultados if r[0] is not None]
    if len(valores) == 0: return 0.0
    return sum(valores) / len(valores)

def gerar_insight_categoria(categoria):
    """Compara o gasto atual com a média histórica."""
    media = calcular_media_historica(categoria)
    # Aqui simularemos o gasto atual 
    # Por simplicidade usaremos a lógica de que se o gasto > média * 1.2 (20% acima), é um alerta.

    return media