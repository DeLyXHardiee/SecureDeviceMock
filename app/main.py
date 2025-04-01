from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import init_db, get_db
from app.scheduler import start_scheduler
from app.external import router as mock
from app.models import Incident
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(mock, prefix="/external")

@app.on_event("startup")
async def startup():
    init_db()
    start_scheduler()

@app.get("/")
def health_check():
    return {"status": "running"}

@app.get("/incidents")
def get_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).order_by(Incident.id).all()

@app.get("/incidents/{incident_id}")
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    return incident

@app.patch("/incidents/{incident_id}")
def update_incident(incident_id: int, incident_data: dict, db: Session = Depends(get_db)):
    existing_incident = db.query(Incident).filter(Incident.id == incident_id).first()
    
    if not existing_incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    for key, value in incident_data.items():
        if hasattr(existing_incident, key):
            setattr(existing_incident, key, value)
    
    db.commit()
    
    db.refresh(existing_incident)
    
    logger.info(f"Updated incident {incident_id}")
    
    return existing_incident