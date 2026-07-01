import enum
from sqlalchemy import Boolean, Column, Integer, String, Text, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key= True, index=True )
    role_id = Column(Integer,ForeignKey("roles.id"),nullable=False )
    role = relationship("Role")
    first_name= Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now(),nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(),nullable=False)
