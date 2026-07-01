from sqlalchemy import Boolean, Column, Identity, Integer, String, Text, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import ENUM, JSONB, INET

audit_logs_enum = ENUM(
    'create',
    'update',
    'delete',
    'login',
    'logout',
    name='audit_action',
    create_type=True
)

class AuditLog(Base):

    __tablename__ = 'audit_logs'

    id = Column(Integer, Identity(always=True), primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action_type = Column(audit_logs_enum, nullable=False)
    entity = Column(String(100), nullable=False)
    entity_id = Column(Integer)
    old_data = Column(JSONB)
    new_data = Column(JSONB)
    ip_address = Column(INET)
    created_at = Column(TIMESTAMP, server_default=func.now(),nullable=False)