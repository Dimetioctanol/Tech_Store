import enum
from sqlalchemy import Boolean, CheckConstraint, Column, Integer, String, Text, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    category_id =Column(Integer,ForeignKey("categories.id"), nullable=False)
    category = relationship("Category")
    name = Column(String(100), nullable=False)
    description = Column(Text)
    sku = Column(String(100), nullable=False, unique=True)
    price = Column(Numeric(10,2), nullable=False)
    cost_product = Column(Numeric(10,2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean,nullable=False, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now(),nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(),nullable=False)


    __table_args__ = (
        CheckConstraint('price > 0', name='check_price_positive'),
        CheckConstraint('cost_product > 0', name='check_cost_positive'),
        CheckConstraint('stock >= 0', name='check_stock_non_negative'),
    )
    
    @validates('price')
    def validate_price(self, key, value):
        if value is not None and value <= 0:
            raise ValueError("El precio no puede ser negativo")
        return value
    @validates('cost_product')
    def validate_cost_product(self, key, value):
        if value is not None and value <= 0:
            raise ValueError("El costo del producto no puede ser negativo")
        return value
    @validates('stock')
    def validate_stock(self,key,value):
        if value is not None and value < 0:
            raise ValueError("EL stock no puede ser negativo")
        return value
        