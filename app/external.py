from fastapi import APIRouter
import random

router = APIRouter()

SEVERITY_CHOICES = ["LOW", "MEDIUM", "HIGH"]
STATUS_CHOICES = ["OPEN", "CLOSED", "ON_HOLD"]
ALARM_TITLES = [
    "Employee Credential Detection (Hacker Forum)",
    "Phishing Campaign Detected",
    "Suspicious Network Activity",
]
ALARM_TYPES = [42, 69, 420]
ASSIGNEES = ["security@test.com", "admin@test.com"]
TAGS = ["botnet", "ransomware"]
MAIN_TYPES = ["brand protection", "network security"]
SUB_TYPES = ["PII Exposure", "Unauthorized Access"]

def generate_mock_incidents():
    return [
        {
            "id": random.randint(1, 50),
            "status": random.choice(STATUS_CHOICES),
            "severities": [random.choice(SEVERITY_CHOICES)],
            "alarm_type_ids": [random.choice(ALARM_TYPES)],
            "assignees": [random.choice(ASSIGNEES)],
            "tags": [random.choice(TAGS)],
            "alarm_main_types": [random.choice(MAIN_TYPES)],
            "alarm_sub_types": [random.choice(SUB_TYPES)],
            "alarm_title": random.choice(ALARM_TITLES),
        }
        for _ in range(2)
    ]

@router.get("/mock-incidents")
def get_mock_incidents():
    return generate_mock_incidents()