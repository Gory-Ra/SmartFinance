from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class Transacao(Base):
    __tablename__ = 'transacoes'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    valor = Column(Float)
    tipo = Column(String) # 'Receita' ou 'Despesa'
    categoria = Column(String)
    data = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Transacao(descricao='{self.descricao}', valor={self.valor}, tipo='{self.tipo}')>"