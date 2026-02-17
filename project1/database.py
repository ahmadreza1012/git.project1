from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , declarative_base
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/tasks')
engine = create_engine(DATABASE_URL, echo=True , connect_args={"check_same_thread" : False})
session_local = sessionmaker(autocommit= False , autoflush=False , bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()