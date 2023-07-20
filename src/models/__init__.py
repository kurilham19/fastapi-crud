from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from src.config.env import DB_URL

# DB_URL = 'sqlite:///./learn_dev.db'
engine = create_engine(
    DB_URL 
    # connect_args={"check_same_thread": False}, 
    # echo=False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# class Base(DeclarativeBase):
#     pass

# Dependency
def get_db() -> SessionLocal:
  try:
      db = SessionLocal()
      yield db
  finally:
      db.close()
