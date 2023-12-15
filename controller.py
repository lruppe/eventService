import uuid
from typing import List

from fastapi import FastAPI
from fastapi import HTTPException

import event_service
from event_service import Event

app = FastAPI()

@app.get("/events", response_model=List[str])
async def get_events():
    return event_service.get_events()

@app.get("/events/{uuid}", response_model=Event)
async def get_events_with_details(uuid: uuid.UUID):
    event = event_service.get_event_with_details(uuid)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


