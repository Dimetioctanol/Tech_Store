from sqlalchemy import Boolean, Column, Identity, Integer, String, Text, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import ENUM, JSONB, INET


order_status_enum = ENUM(
    'pending',
    'paid',
    'shipped',
    'delivered',
    'cancelled',
    name = 'order_status',
    create_type = True
)

class Order(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer,ForeignKey('users.id'), nullable=False)
    status = Column(order_status_enum, nullable=False, default='pending')
    total_amount = Column(Numeric(12,2),nullable=False,default=0 )
    created_at = Column(TIMESTAMP, server_default=func.now(),nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(),nullable=False)
