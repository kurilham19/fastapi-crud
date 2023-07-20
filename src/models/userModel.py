from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from . import Base

class UserModel(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  email = Column(String)
  password = Column(String)
  created_at = Column(DateTime, server_default=func.now())
  updated_at = Column(DateTime,onupdate=func.now())
  
  # id: Mapped[int] = mapped_column(primary_key=True, index=True)
  # name: Mapped[str]
  # email: Mapped[str]
  # password: Mapped[str]
  # created_at: Mapped[str] = mapped_column(DateTime,server_default=func.now())
  # created_at: Mapped[str] = mapped_column(DateTime,onupdate=func.now())
  