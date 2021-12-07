import requests
from bs4 import BeautifulSoup
import json


list_categories = []

THERMAL_EQUIPMENT_CATEGORIES_JSON = 'kiy_v_json/thermal_equipment_categories.json'


def parser_categories(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    category_blocks = soup.find_all('div', {'class', 'grid-item normal category'})

    for categories in category_blocks:
        list_categories.append(
            {
                'Name category': categories.find('a').find('span').text.strip('\n'),
                'URL category': categories.find('a').get('href'),
                'Image category': categories.find('a').find('img').get('data-src'),
            }
        )

    with open(THERMAL_EQUIPMENT_CATEGORIES_JSON, 'w') as file:
            json.dump(list_categories, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    parser_categories('https://www.kiy-v.ua/ua/teplove-obladnannja.html')