import uuid

#read both files in
with open('events.txt', 'r', encoding='utf-8') as f:
    events = f.readlines()

with open('events_details.txt', 'r', encoding='utf-8') as f:
    events_with_details = f.readlines()

events_consolidated = []
for i in range(len(events)):
    events[i] = events[i].strip()
    events_with_details[i] = events_with_details[i].strip()

    name, description, url = events[i].split(';')
    name, details, dates, url = events_with_details[i].split(';')
    if name != name:
        print("Error: names do not match")
    if name == '' or details == '' or dates == '' or url == '':
        print("Error: something is empty")

    event = f'{uuid.uuid4()}; {name}; {description}; {details}; {dates}; {url}'
    events_consolidated.append(event)
    print(event)

with open('events_consolidated.txt', 'w', encoding='utf-8') as f:
    for consolidatedevent in events_consolidated:
        f.write(consolidatedevent + '\n')