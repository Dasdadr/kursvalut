import requests
from bs4 import BeautifulSoup

base_url = 'https://www.akchabar.kg/ru/exchange-rates/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title)




msgs = soup.select('tbody')
print(msgs)