from sqlalchemy import Column, Integer, String, ForeignKey, Boolean as Bool, Float
from datetime import datetime, timezone
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

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


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(Bool, nullable=False, default=False)
    total_amount = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime(), nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),server_onupdate=func.now(),nullable=False)

    user = relationship("User", back_populates="orders")

