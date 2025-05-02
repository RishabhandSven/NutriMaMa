from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from app.services.alert_service import send_alert

router = APIRouter()

class EmergencyAlert(BaseModel):
    patient_id: str = Field(..., description="The ID of the patient")
    alert_type: str = Field(..., description="Type of emergency alert")
    description: Optional[str] = Field(None, description="Description of the alert")
    location: str = Field(..., description="GPS location of the alert")

@router.post("/alert")
async def create_alert(alert: EmergencyAlert):
    try:
        await send_alert(alert)
        return {"message": "Emergency alert submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))