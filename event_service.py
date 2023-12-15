import uuid
from typing import List, Optional

from pydantic import BaseModel, UUID4


class Event(BaseModel):
    uuid: UUID4
    title: str
    description: str
    details: str
    dates: str
    link: str

    def get_basic_info(self) -> str:
        return f'{self.uuid}; {self.title}; {self.description}; {self.dates}; {self.link}'

    # def get_detailed_information(self) -> Event:
    #     return {
    #         "uuid" : self.uuid,
    #         "title" : self.title,
    #         "details" : self.details
    #     }


with open('data/events_consolidated.txt', 'r', encoding='utf-8') as f:
    events_with_details = f.readlines()

events = []
for line in events_with_details:
    event_id, name, description, details, dates, url = [item.strip() for item in line.split(';')]
    event = Event(uuid=event_id, title=name, description = description, details = details, dates = dates, link = url)
    events.append(event)


def get_event_with_details(event_uuid: uuid.UUID) -> Optional[Event]:
    for candidate in events:
        if candidate.uuid == event_uuid:
            return candidate
    return None


def get_events() -> List[str]:
    return [event.get_basic_info() for event in events]


if __name__ == '__main__':
    for event in get_events():
        print(event)

    print(get_event_with_details(uuid.UUID("308f430e-6284-4640-a219-f3cb5c7cd4ff")))