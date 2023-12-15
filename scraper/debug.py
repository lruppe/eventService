import requests
from bs4 import BeautifulSoup

respone = requests.get(
    'https://www.myswitzerland.com/de-ch/erlebnisse/veranstaltungen/buere-noeijohr-2024-fasnacht-bueren-an-der-aare-2024/')



# Parse the HTML
soup = BeautifulSoup(respone.text, 'html.parser')

# Extract the short description
short_description = soup.find('div', class_='LeadText--text').get_text(strip=True)

# Navigate to the correct 'richtext' for the long description
article_section_plain = soup.find('div', class_='ArticleSection plain')
long_description_div = article_section_plain.find('div', class_='richtext')
long_description = long_description_div.get_text(strip=True)

# Extract the first occurrence of dates
first_dates_div = soup.find('div', class_='SidebarWidget--body')
dates = first_dates_div.p.get_text(strip=True)

# Print the extracted information
print("Short Description:", short_description)
print("Long Description:", long_description)
print("Dates:", dates)
