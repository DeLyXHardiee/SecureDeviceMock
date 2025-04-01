from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from app.models import Incident
from app.database import SessionLocal

import logging
import requests

logger = logging.getLogger(__name__)

EXTERNAL_SERVICE_URL = "http://localhost:8000/external/mock-incidents"

def save_incidents_to_db(incidents, db):
    for incident_data in incidents:
        existing_incident = db.query(Incident).filter(Incident.id == incident_data["id"]).first()
        
        if existing_incident:
            updated = False 
            
            for key, value in incident_data.items():
                if getattr(existing_incident, key) != value:
                    setattr(existing_incident, key, value)
                    updated = True

            if updated:
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
        logger.info("Polling incidents from external mock service...")
        
        response = requests.get(EXTERNAL_SERVICE_URL)
        response.raise_for_status() 
        
        incidents = response.json()
        logger.info(f"Fetched {len(incidents)} incidents.")

        save_incidents_to_db(incidents, db)
        logger.info("Poll successful!")
    except requests.RequestException as e:
        logger.error(f"Error fetching incidents: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        db.close()

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Interval style polling for testing
    scheduler.add_job(
        poll_incidents, 'interval', seconds=10
    )
    # Uncomment below for cron style polling
    '''scheduler.add_job(
        poll_incidents, 'cron', hour=12
    )'''
    scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()

def job_listener(event):
    if event.exception:
        logger.error(f"Job failed: {event.job_id}")
    else:
        logger.info(f"Job executed successfully: {event.job_id}")
