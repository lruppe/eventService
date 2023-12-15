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

def initial_scrape():
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

def get_details(url, session):
    respone = session.get(url)
    soup = BeautifulSoup(respone.text, 'html.parser')

    # Extract the short description
    short_description_div = soup.find('div', class_='LeadText--text')
    if short_description_div is None:
        short_description = ''
    else:
        short_description = short_description_div.get_text(strip=True)

    # Navigate to the correct 'richtext' for the long description
    article_section_plain = soup.find('div', class_='ArticleSection plain')
    long_description_div = article_section_plain.find('div', class_='richtext')
    # add a try catch block to handle the case where there is no description or dates
    if long_description_div is None:
        long_description = ''
    else:
        long_description = long_description_div.get_text(strip=True)

    # Extract the first occurrence of dates
    first_dates_div = soup.find('div', class_='SidebarWidget--body')

    if first_dates_div is None:
        dates = ''
    else:
        dates = first_dates_div.p.get_text(strip=True)

    return {
        'description': short_description + '\n' + long_description,
        'dates': dates
    }

if __name__ == '__main__':
    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (compatible; events/1.0)'
    })

    with open('events.txt', 'r') as f:
        events = f.readlines()
    event_with_deatils = []
    for event in events:
        event = event.strip()
        title, description_overview, link = event.split(';')
        # scrape details
        details = get_details(link, session)

        # clean
        dates = details['dates'].replace(';', ',')
        description = details['description'].replace(';', ',').replace('\n', ' ')

        # append the title, description, dates and link to event_with_deatils
        event_with_deatils.append(f"{title}; {description}; {dates}; {link}")
        print(f"{title}; {description}; {dates}; {link}")

    # print the title, descrption, deatils, dates and link to a file, ;-separated, utf-8 encoded
    with open('events_details.txt', 'w', encoding='utf-8') as f:
        for event in event_with_deatils:
            f.write(event + '\n')