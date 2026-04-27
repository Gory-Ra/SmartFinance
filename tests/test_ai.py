from database import engine
from sqlalchemy import inspect

inspector = inspect(engine)
print(f"Tabelas encontradas: {inspector.get_table_names()}")