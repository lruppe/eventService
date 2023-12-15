import requests

respone = requests.get(
    'https://www.myswitzerland.com/de-ch/erlebnisse/veranstaltungen/veranstaltungen-suche/?Datum_from=2024-01-02&Datum_to=2024-02-29&rubrik=topveranstaltungen&p=2&noidx=1')
print(respone.text)

respone4 = requests.get(
    'https://www.myswitzerland.com/de-ch/erlebnisse/veranstaltungen/veranstaltungen-suche/?Datum_from=2024-01-02&Datum_to=2024-02-29&rubrik=topveranstaltungen&p=3&noidx=1')
print(respone4.text)

respone4 = requests.get(
    'https://www.myswitzerland.com/de-ch/erlebnisse/veranstaltungen/veranstaltungen-suche/?Datum_from=2024-01-02&Datum_to=2024-02-29&rubrik=topveranstaltungen&p=4&noidx=1')
print(respone4.text)