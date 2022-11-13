import requests
from bs4 import BeautifulSoup

base_url = 'https://www.akchabar.kg/ru/exchange-rates/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')



msgs = soup.find('div', {'class' : 'col-md-9'})
msgs = msgs.text
print(msgs)
#
# # with open("hello.txt", "w") as file:
# #     file.write(msgs)


# url = 'https://www.akchabar.kg/ru/exchange-rates/'
#
# source = requests.get(url)
# main_text = source.text
# soup = BeautifulSoup(main_text, 'html.parser')
#
# table = soup.find('div', {'class': 'row'})
# td = table.find('div', {'class': 'col-md-9'})
# td1 = table.find('td')
# td = td.text
#
# td1 = td1.text
#
#
# print(td)
# print(td1)
