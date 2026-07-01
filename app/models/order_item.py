from sqlalchemy import Boolean, CheckConstraint, Column, Identity, Integer, String, Text, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import ENUM, JSONB, INET

class OrderItem(Base):

    __tablename__ = 'order_items'

    id = Column(Integer,primary_key=True,index=True )
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer,ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10,2), nullable=False)
    subtotal = Column(Numeric(10,2), nullable=False)

    __table_args__ = (
        CheckConstraint('quantity > 0', name='check_quantity_order_positive'),
        CheckConstraint('unit_price > 0', name='check_unit_price_positive'),
        CheckConstraint('subtotal >= 0', name='check_subtotal_non_negative'),
    )

    @validates('quantity')
    def validate_quantity(self,key,value):
        if value is not None and value <=0:
            raise ValueError('La cantidad no puede ser negativa')
        return value
    
    @validates('unit_price')
    def validate_unit_price(self,key,value):
        if value is not None and value <=0:
            raise ValueError('El precio de unidad no puede ser negativo')
        return value
    
    @validates('subtotal')
    def validate_unit_price(self,key,value):
        if value is not None and value <=0:
            raise ValueError('El subtotal no puede ser negativo')
        return value
