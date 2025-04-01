from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from datetime import datetime
import logging
import requests

from app.models import Incident
from app.database import SessionLocal, get_db

logger = logging.getLogger(__name__)

def fetch_incidents_from_external_service():
    mock_incidents = [
        {"id": 1, "status": "New"},
        {"id": 2, "status": "Resolved"}
    ]
    return mock_incidents

def save_incidents_to_db(incidents, db):
    for incident_data in incidents:
        existing_incident = db.query(Incident).filter(Incident.id == incident_data["id"]).first()
        
        if existing_incident:
            if existing_incident.status != incident_data["status"]:
                existing_incident.status = incident_data["status"]
                db.commit()
                logger.info(f"Updated incident {incident_data['id']}")
            else:
                logger.info(f"Incident {incident_data['id']} not in need of update")                
        else:
            new_incident = Incident(**incident_data)
            db.add(new_incident)
            db.commit()
            logger.info(f"Created new incident {incident_data['id']}")

def poll_incidents():
    db = SessionLocal()
    try:
        incidents = fetch_incidents_from_external_service()
        save_incidents_to_db(incidents, db)
    finally:
        db.close()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        poll_incidents, 'interval', seconds=5
    )
    scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()

def job_listener(event):
    if event.exception:
        logger.error(f"Job failed: {event.job_id}")
    else:
        logger.info(f"Job executed successfully: {event.job_id}")
