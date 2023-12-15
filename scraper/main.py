# This is a sample Python script.
import requests
from bs4 import BeautifulSoup


def format_event(event):
    return f"{event['title']}; {event['description']}; {event['link']}"

# Press the green button in the gutter to run the script.
def get_events(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    extracted_data = []
    events = soup.find_all('li', class_='FilterMap--teaserList--item js-slider--slide')

    for event in events:
        try:
            title = event.find('h3', class_='OfferTeaser--title').text.strip()
            description = event.find('div', class_='OfferTeaser--text').text.strip()

            link = event.find('a', class_='OfferTeaser--link')['href']
            extracted_data.append({
                'title': title,
                'description': description,
                'link': link
            })
        except:
            print(event)


    return extracted_data

if __name__ == '__main__':
    events = []
    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (compatible; events/1.0)'
    })

    response = session.get('https://www.myswitzerland.com/de-ch/erlebnisse/veranstaltungen/veranstaltungen-suche/?Datum_from=2024-01-02&Datum_to=2024-02-29&rubrik=topveranstaltungen&noidx=1')
    events_per_page = get_events(response)
    events.extend(events_per_page)

    for i in range(2,11):
        url = 'https://www.myswitzerland.com/de-ch/erlebnisse/veranstaltungen/veranstaltungen-suche/?Datum_from=2024-01-02&Datum_to=2024-02-29&rubrik=topveranstaltungen&p={}&noidx=1'.format(i)
        print(url)
        response = session.get(url)
        events_per_page = get_events(response)
        events.extend(events_per_page)
    with open('events.txt', 'w') as f:
        for event in events:
            formatted_event = format_event(event)
            f.write(formatted_event + '\n')