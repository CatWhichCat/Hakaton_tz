import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml
from collections import defaultdict


def url_get(
        url='https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'):
    read = requests.get(url)
    # print(read) -> 200
    # pprint(soup.prettify())
    # список имен жив
    animal_names = []
    while True:
        html = read.content
        soup = BeautifulSoup(html, 'lxml')
        get_teg = soup.find('div', id='mw-pages').find(
            'div', class_='mw-category-group').find('ul').find_all('a')
        # итерируются элементы и расширяется список
        animal_names.extend(list(map(lambda x: x.text, get_teg)))
        next_page = soup.find(id='mw-pages').find('a',
                                                  text='Следующая страница')
        if not next_page:
            break
        # pprint(next_page)
        read = requests.get('https://ru.wikipedia.org' + next_page['href'])
        names_count_first_letter = defaultdict(int)
        for names_animals_amount in animal_names:
            names_count_first_letter[names_animals_amount[0]] += 1
        pprint(names_count_first_letter)


url_get()