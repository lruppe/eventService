import re
import uuid
from datetime import datetime


def parse_german_date(date_str):
    if date_str == '':
        return datetime(2023, 1, 1).strftime('%Y-%m-%d'), datetime(2024, 1, 1).strftime('%Y-%m-%d')
    # Define German month names to numbers mapping
    month_mapping = {
        "Januar": 1, "Februar": 2, "März": 3, "April": 4, "Mai": 5, "Juni": 6,
        "Juli": 7, "August": 8, "September": 9, "Oktober": 10, "November": 11, "Dezember": 12
    }

    # Check for date range format (Type 3)
    if '-' in date_str:
        start_date, end_date = date_str.split(' - ')
        if len(start_date) == 2:
            start_date = start_date + end_date[2:]
        else:
            start_date = start_date + " " + end_date[-4:]
        return parse_german_date(start_date), parse_german_date(end_date)

    # Extract day and month-year part
    parts = re.split(r'\s+', date_str)
    if len(parts) == 3:
        # Format: 12 - 14. Januar 2024
        day = int(parts[0].rstrip('.'))
        month_year = parts[1:]
    else:
        # Format: 13. Januar 2024
        day = int(parts[0][:-1])
        month_year = parts[1:]

    month = month_mapping[month_year[0]]
    year = int(month_year[1])
    start_and_enddate = datetime(year, month, day).strftime('%Y-%m-%d')
    # Return the date in a standardized format
    return start_and_enddate


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

    dates_formatted = parse_german_date(dates.strip())
    if len(dates_formatted) != 2:
        event = f'{uuid.uuid4()}; {name}; {description}; {details}; {dates_formatted}; {dates_formatted}; {url}'
    else:
        event = f'{uuid.uuid4()}; {name}; {description}; {details}; {dates_formatted[0]}; {dates_formatted[1]}; {url}'
    events_consolidated.append(event)
    print(event)

with open('events_consolidated1.txt', 'w', encoding='utf-8') as f:
    for consolidatedevent in events_consolidated:
        f.write(consolidatedevent + '\n')