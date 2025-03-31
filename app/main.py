from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.schemas import IncidentFilter
from app.database import init_db
from app.database import get_db
from app import crud



app = FastAPI()

init_db()

@app.get("/")
def health_check():
    return {"status": "running"}

from app import crud
@app.post("/incidents/")
def create_incident(filter: IncidentFilter, db: Session = Depends(get_db)):
    incident_data = filter.dict()
    db_incident = crud.create_incident(db=db, incident_data=incident_data)
    return {"message": "Incident created", "incident": db_incident.id}