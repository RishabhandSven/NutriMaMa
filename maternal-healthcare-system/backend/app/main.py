from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import emergency_alert, user_log

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(emergency_alert.router)
app.include_router(user_log.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Maternal Healthcare System API"}