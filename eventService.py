
def get_events():
    with open('events.txt', 'r') as f:
        events = f.readlines()
    return events


if __name__ == '__main__':
    events = get_events()
    for event in events:
        print(event)