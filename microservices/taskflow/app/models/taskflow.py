from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from datetime import datetime

from app.db.base import Base

class Taskflow(Base):
    __tablename__ = "taskflows"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    end_date = Column(DateTime, nullable=True)  # Campo para la fecha de finalización (opcional)
    tags = Column(String, nullable=True) 
    completed = Column(Boolean, default=False) 

    def __repr__(self):
        return f"<Taskflow(id={self.id}, title={self.title}, description={self.description})>"

