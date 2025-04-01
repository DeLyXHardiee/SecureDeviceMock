from sqlalchemy.orm import Session
from app.models import Incident
from datetime import date
import json

def create_incident(db: Session, incident_data: dict):
    db_incident = Incident(
        alarm_type_ids=json.dumps(incident_data.get("alarm_type_ids", [])), 
        excluded_alarm_type_ids=json.dumps(incident_data.get("excluded_alarm_type_ids", [])),
        notification_ids=json.dumps(incident_data.get("notification_ids", [])),
        alarm_ids=json.dumps(incident_data.get("alarm_ids", [])),

        status=incident_data.get("status", "UNKNOWN"),  
        assignees=json.dumps(incident_data.get("assignees", [])),
        excluded_assignees=json.dumps(incident_data.get("excluded_assignees", [])),

        tags=json.dumps(incident_data.get("tags", [])),
        excluded_tags=json.dumps(incident_data.get("excluded_tags", [])),

        alarm_main_types=json.dumps(incident_data.get("alarm_main_types", [])),
        excluded_alarm_main_types=json.dumps(incident_data.get("excluded_alarm_main_types", [])),

        alarm_sub_types=json.dumps(incident_data.get("alarm_sub_types", [])),
        excluded_alarm_sub_types=json.dumps(incident_data.get("excluded_alarm_sub_types", [])),

        alarm_title=json.dumps(incident_data.get("alarm_title", [])),
        excluded_alarm_title=json.dumps(incident_data.get("excluded_alarm_title", [])),

        severities=json.dumps(incident_data.get("severities", [])),  

        created_at=incident_data.get("start_date", date.today()),  
        end_date=incident_data.get("end_date", None)  
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident
