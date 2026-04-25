from sqlalchemy import create_all, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria o arquivo do banco localmente
engine = create_engine('sqlite:///financas.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)