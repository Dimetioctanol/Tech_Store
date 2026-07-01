from sqlalchemy import Boolean, CheckConstraint, Column, Identity, Integer, String, Text, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import ENUM, JSONB, INET


movement_type_enum = ENUM(
    'in',
    'out',
    'adjustment',
    name = 'movement_type',
    create_type = True
)


class InventoryMovement(Base):

    __tablename__ = 'inventory_movements'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    products = relationship("Product")
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    users = relationship("User")
    movement_type = Column(movement_type_enum, nullable=False)
    quantity = Column(Integer, nullable=False)
    reason = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now(),nullable=False)

    __table_args__ = (
        CheckConstraint('quantity > 0', name='check_quantity_positive'),
    )

    @validates('quantity')
    def validate_quantity(self,key,value):
        if value is not None and value <=0:
            raise ValueError("La cantidad no puede ser negativa")
        return value