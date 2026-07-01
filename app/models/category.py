import enum
from sqlalchemy import Boolean, Column, Integer, String, Text, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name= Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now(),nullable=False)