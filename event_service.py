import uuid
from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, UUID4


class Event(BaseModel):
    uuid: UUID4
    title: str
    description: str
    details: str
    start_date: date
    end_date: date
    link: str

    def get_basic_info(self) -> str:
        return f'{self.uuid}; {self.title}; {self.description}'

def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%Y-%m-%d').date()

with open('data/events_consolidated1.txt', 'r', encoding='utf-8') as f:
    events_with_details = f.readlines()

events = []
for line in events_with_details:
    event_id, name, description, details, start_str, end_str, url = [item.strip() for item in line.split(';')]
    start_date = parse_date(start_str)
    end_date = parse_date(end_str)
    event = Event(uuid=event_id, title=name, description = description, details = details, start_date = start_date, end_date = end_date, link = url)
    events.append(event)


def get_event_with_details(event_uuid: uuid.UUID) -> Optional[Event]:
    for candidate in events:
        if candidate.uuid == event_uuid:
            return candidate
    return None

def get_events_by_date(target_date: date) -> List[str]:
    if target_date is None or target_date == "":
        return get_all_events()
    else:
        return [
            event.get_basic_info()
            for event in events
            if event.start_date <= target_date and event.end_date >= target_date
        ]

def get_all_events() -> List[str]:
    return [event.get_basic_info() for event in events]


if __name__ == '__main__':
    mydate = date(2024,2,1)
    filtered_dates = get_events_by_date("")
    print(len(filtered_dates))