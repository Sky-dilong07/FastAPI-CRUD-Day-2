from sqlmodel import SQLModel, create_engine

DB_FILE = 'db.sqlite3'
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)
