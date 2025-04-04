
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import asyncio
import random
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model for water parameters
class WaterData(BaseModel):
    timestamp: datetime
    temperature: float
    pH: float
    turbidity: float
    flow_rate: float
    dissolved_oxygen: float

# Store connected clients
clients = set()

# Add a simple test endpoint
@app.get("/")
async def root():
    return {"message": "Water monitoring system is running"}

async def get_water_data():
    """
    Simulate getting data from IoT sensors.
    Replace this with actual IoT sensor data collection code.
    """
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": round(random.uniform(15, 25), 2),  # °C
        "pH": round(random.uniform(6.5, 8.5), 2),
        "turbidity": round(random.uniform(0, 10), 2),  # NTU
        "flow_rate": round(random.uniform(0, 100), 2),  # L/min
        "dissolved_oxygen": round(random.uniform(6, 12), 2),  # mg/L
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    try:
        while True:
            data = await get_water_data()
            await websocket.send_json(data)
            await asyncio.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        clients.remove(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="127.0.0.1",  # Using IPv4 localhost address
        port=8000,
        log_level="info"
    )
