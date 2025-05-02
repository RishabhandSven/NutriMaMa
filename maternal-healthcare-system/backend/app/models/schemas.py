from pydantic import BaseModel
from typing import Optional, List

class Patient(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    address: str
    contact_number: str

class Flag(BaseModel):
    id: str
    patient_id: str
    flag_type: str
    description: str
    timestamp: str

class Observation(BaseModel):
    id: str
    patient_id: str
    observation_type: str
    value: float
    unit: str
    timestamp: str

class UserLog(BaseModel):
    patient_id: str
    blood_pressure: Optional[str] = None
    weight: Optional[float] = None
    symptoms: Optional[List[str]] = None
    timestamp: str