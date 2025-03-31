from sqlalchemy.orm import Session
from app.models import Incident
from datetime import date

def create_incident(db: Session, incident_data: dict):
    db_incident = Incident(
        alarm_type_ids=incident_data["alarm_type_ids"],
        status=incident_data["status"],
        assignees=incident_data["assignees"],
        tags=incident_data["tags"],
        alarm_main_types=incident_data["alarm_main_types"],
        alarm_sub_types=incident_data["alarm_sub_types"],
        alarm_title=incident_data["alarm_title"],
        severities=incident_data["severities"],
        created_at=incident_data.get("start_date", date.today())
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident