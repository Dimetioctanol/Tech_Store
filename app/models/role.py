from sqlalchemy import Boolean, Column, Identity, Integer, String, Text, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import ENUM, JSONB, INET

class Role(Base):
    __tablename__ = "roles"

    id= Column(Integer, primary_key = True, index=True)
    name = Column(String(100), nullable= False, unique=True)
    description = Column(Text, nullable=True)
    created_at = Column (TIMESTAMP, server_default = func.now(), nullable=False)
