import requests
from bs4 import BeautifulSoup

def get_counttries():
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%BC%D0%B8%D1%80%D0%B0'
    responce = requests.get(url)
    soap = BeautifulSoup(responce.text, 'lxml')
    div = soap.find_all('div', attrs={'class': 'columns'})
    div.pop()
    cites = set()
    for i in div:
        p = i.text.split('\n')
        p.pop(0)
        for j in p:
            x = j.find('[')
            if x != -1:
                j = j[:x]
            j = j.lstrip()
            cites.add(j)
    cites.discard('')
    return cites

