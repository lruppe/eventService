import uuid
from datetime import date
from typing import List

from fastapi import FastAPI
from fastapi import HTTPException

import event_service
from event_service import Event

app = FastAPI()


@app.get("/events", response_model=List[str])
async def get_all_events():
    """
    Retrieves a list of events

    Args:
        none

    Returns:
        A list of events including their basic information.
    """
    return event_service.get_all_events()


@app.get("/events/{target_uuid}", response_model=Event)
async def get_events_with_details(target_uuid: uuid.UUID):
    """
    Retrieves a detailed description of an event

    Args:
        target_id (uuid): The ID of the item to retrieve.

    Returns:
        An event including its detailed information.

    """
    event = event_service.get_event_with_details(target_uuid)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@app.get("/events/by-date/{target_date}", response_model=List[str])
async def get_events_by_date(target_date: date):
    """
    Retrieves a list of events happening on a specific date

    Args:
        target_date (date): The date in format "YYYY-MM-DD"

    Returns:
        A list of events on the target date including their basic information.
    """
    return event_service.get_events_by_date(target_date)
