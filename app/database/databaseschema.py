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

    # one-to-many: a user has many orders
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, server_default='0')

    # association objects (OrderItem)
    order_items = relationship("OrderItem", back_populates="product", cascade="all, delete-orphan")
    # convenience many-to-many (read-only) via association table
    orders = relationship("Order", secondary="order_items", back_populates="products", viewonly=True)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(Bool, nullable=False, default=False)
    total_amount = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # one-to-many: order -> user
    user = relationship("User", back_populates="orders")

    # association objects linking to products
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    # convenience many-to-many (read-only)
    products = relationship("Product", secondary="order_items", back_populates="orders", viewonly=True)


class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default='1')
    unit_price = Column(Float, nullable=False, default=0.0)

    # association object relationships
    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")