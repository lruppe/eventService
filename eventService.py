with open('events_details.txt', 'r', encoding='utf-8') as f:
    events_with_details = f.readlines()

with open('events.txt', 'r', encoding='utf-8') as f:
    events = f.readlines()

def get_events_with_details():
    return events_with_details
def get_events():
    return events


if __name__ == '__main__':
    events_with_details = get_events_with_details()
    for event in events_with_details:
        print(event)