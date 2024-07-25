from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

app = FastAPI()

# Data model for sensor data
class SensorData(BaseModel):
    temperature: float
    moisture: float
    light: float
    timestamp: str = None

# In-memory storage for sensor data
data_log: List[Dict] = []

@app.post("/api/sensor_data")
async def log_sensor_data(data: SensorData):
    data.timestamp = datetime.now().isoformat()
    data_log.append(data.dict())
    return {"status": "success", "data": data}

@app.get("/api/sensor_data")
async def get_sensor_data():
    return {"status": "success", "data": data_log}

@app.get("/")
async def root():
    return {"message": "Sensor Data API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
