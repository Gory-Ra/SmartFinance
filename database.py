import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Pega a pasta onde o database.py está localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Define o caminho completo para o banco
db_path = os.path.join(BASE_DIR, 'financas.db')

engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    # O create_all é chamado aqui, através do Base.metadata
    Base.metadata.create_all(engine)
    # Pega a pasta onde o database.py está localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Define o caminho completo para o banco
db_path = os.path.join(BASE_DIR, 'financas.db')

engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)
Base = declarative_base()