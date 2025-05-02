def validate_bp(systolic: int, diastolic: int) -> bool:
    if 90 <= diastolic <= 120 and 60 <= systolic <= 180:
        return True
    return False

def format_alert_message(patient_id: str, alert_type: str, details: str) -> str:
    return f"Alert for Patient ID {patient_id}: {alert_type} - {details}"

def parse_user_log(data: dict) -> dict:
    return {
        "blood_pressure": data.get("blood_pressure"),
        "weight": data.get("weight"),
        "symptoms": data.get("symptoms"),
        "timestamp": data.get("timestamp")
    }