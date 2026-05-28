# 从第 29 章提取
# 来源：Codex 从入门到项目实践

from sqlalchemy import (
    Column, Integer, String, Text, DECIMAL, DateTime,
    ForeignKey, CheckConstraint, Table
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

# 多对多关联表（Product ↔ Supplier）
product_supplier = Table(
    'product_supplier', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('supplier_id', Integer, ForeignKey('suppliers.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(20), default='user')
    phone = Column(String(20))
    orders = relationship('Order', back_populates='user')

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = (
        CheckConstraint('unit_price >= 0', name='ck_product_price'),
    )
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    sku = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    is_deleted = Column(Integer, default=0)
    inventory = relationship('Inventory', back_populates='product', uselist=False)
    suppliers = relationship('Supplier', secondary=product_supplier, back_populates='products')
    order_items = relationship('OrderItem', back_populates='product')

class Inventory(Base):
    __tablename__ = 'inventory'
    __table_args__ = (
        CheckConstraint('current_quantity >= 0', name='ck_inv_current'),
        CheckConstraint('locked_quantity >= 0', name='ck_inv_locked'),
    )
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), unique=True, nullable=False)
    current_quantity = Column(Integer, nullable=False, default=0)
    locked_quantity = Column(Integer, nullable=False, default=0)
    safety_threshold = Column(Integer, nullable=False, default=10)
    product = relationship('Product', back_populates='inventory')

class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = (
        CheckConstraint(
            "status IN ('pending_payment','paid','shipped','completed','cancelled')",
            name='ck_order_status'
        ),
    )
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_no = Column(String(32), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String(20), nullable=False, default='pending_payment')
    total_amount = Column(DECIMAL(10, 2), nullable=False, default=0)
    address = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='orders')
    items = relationship('OrderItem', back_populates='order')

class OrderItem(Base):
    __tablename__ = 'order_items'
    __table_args__ = (
        CheckConstraint('quantity > 0', name='ck_orderitem_qty'),
    )
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price_snapshot = Column(DECIMAL(10, 2), nullable=False)
    order = relationship('Order', back_populates='items')
    product = relationship('Product', back_populates='order_items')

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    contact_person = Column(String(50))
    phone = Column(String(20))
    status = Column(String(20), default='active')
    products = relationship('Product', secondary=product_supplier, back_populates='suppliers')