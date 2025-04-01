from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.schemas import IncidentFilter
from app.database import SessionLocal, init_db, get_db
from app import crud
from app.scheduler import start_scheduler
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
async def startup():
    init_db()
    start_scheduler()

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/incidents/")
def create_incident(filter: IncidentFilter, db: Session = Depends(get_db)):
    incident_data = filter.dict()
    db_incident = crud.create_incident(db=db, incident_data=incident_data)
    return {"message": "Incident created", "incident": db_incident.id}


# Put below external mock in its own file?
class IncidentMockResponse(BaseModel):
    id: int
    status: str

@app.get("/mock-external-service/incidents", response_model=list[IncidentMockResponse])
async def get_mock_incidents():
    return [
        {"id": 1, "status": "New"},
        {"id": 2, "status": "Resolved"}
    ]