from typing import List
from fastapi import FastAPI
import eventService

app = FastAPI()

@app.get("/events", response_model=List[str])
async def get_events():
    return eventService.get_events()

@app.get("/eventsWithDetails", response_model=List[str])
async def get_events():
    return eventService.get_events_with_details()

