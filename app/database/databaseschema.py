from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    phno = Column(String(15), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    role = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)
    password = Column(String(255), nullable=False, default='abcd@1234')

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, server_default='0')