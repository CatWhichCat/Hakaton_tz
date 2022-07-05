import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml


def url_get(
        url='https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'):
    read = requests.get(url)
    # print(read) -> 200
    # pprint(soup.prettify())
    animal_names = []
    while True:
        html = read.content
        soup = BeautifulSoup(html, 'lxml')
        get_teg = soup.find('div', id='mw-pages').find(
            'div', class_='mw-category-group').find('ul').find_all('a')
        animal_names.extend(list(map(lambda x: x.text, get_teg)))
        next_page = soup.find(id='mw-pages').find('a',
                                                  text='Следующая страница')
        if not next_page:
            break
        # pprint(next_page)
        read = requests.get('https://ru.wikipedia.org' + next_page['href'])
    pprint(animal_names[-50:])
    # pprint(next_page)


url_get()