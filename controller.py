import uuid
from typing import List

from fastapi import FastAPI
from fastapi import HTTPException

import event_service
from event_service import Event

app = FastAPI()

@app.get("/events", response_model=List[str])
async def get_events():
    """
    Retrieves a list of events

    Args:
        none

    Returns:
        A list of events including their basic information.
    """
    return event_service.get_events()

@app.get("/events/{uuid}", response_model=Event)
async def get_events_with_details(uuid: uuid.UUID):
    """
    Retrieves a detailed description of an event

    Args:
        item_id (int): The ID of the item to retrieve.

    Returns:
        An event including its detailed information.
    """
    event = event_service.get_event_with_details(uuid)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


