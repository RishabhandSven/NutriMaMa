from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class UserLog(BaseModel):
    blood_pressure: str
    weight: float
    symptoms: List[str]

@router.post("/log")
async def log_user_data(user_log: UserLog):
    # Here you would typically save the user log data to a database
    # For now, we will just return the received data
    return {"message": "User data logged successfully", "data": user_log}