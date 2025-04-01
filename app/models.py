from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    alarm_type_ids = Column(JSONB)
    status = Column(String, index=True)
    assignees = Column(JSONB)
    tags = Column(JSONB)
    alarm_main_types = Column(JSONB)
    alarm_sub_types = Column(JSONB)
    alarm_title = Column(String)
    severities = Column(JSONB) 
    created_at = Column(DateTime, default=datetime.now)