from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///financas.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    # O create_all é chamado aqui, através do Base.metadata
    Base.metadata.create_all(engine)