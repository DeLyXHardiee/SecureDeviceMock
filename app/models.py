from sqlalchemy import Column, Integer, String, Date, JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class SeverityEnum(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class Incident(Base):
    __tablename__ = 'incidents'

    id = Column(Integer, primary_key=True, index=True)
    alarm_type_ids = Column(JSON)
    status = Column(String)
    assignees = Column(JSON)
    tags = Column(JSON)
    alarm_main_types = Column(JSON)
    alarm_sub_types = Column(JSON)
    alarm_title = Column(String)
    severities = Column(Enum(SeverityEnum))
    created_at = Column(Date)

