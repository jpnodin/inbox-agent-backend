from sqlalchemy import Column, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import uuid

Base = declarative_base()
def generate_uuid(): return str(uuid.uuid4())

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, default=generate_uuid)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    tasks = relationship('Task', back_populates='user')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey('users.id'))
    client = Column(String)
    source = Column(String)
    content = Column(Text)
    due_date = Column(DateTime, nullable=True)
    status = Column(String, default='open')
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='tasks')

class AgentRun(Base):
    __tablename__ = 'agent_runs'
    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey('users.id'))
    started_at = Column(DateTime, default=datetime.utcnow)
    duration_ms = Column(String, nullable=True)
    success = Column(Boolean, default=True)
    message = Column(Text, nullable=True)
    user = relationship('User')
