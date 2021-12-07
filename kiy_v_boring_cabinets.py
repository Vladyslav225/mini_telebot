import requests
from bs4 import BeautifulSoup
import json


list_product = []

PC_PRODUCTS_JSON = 'kiy_v_json/pc_products.json'

def parser_product(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    pages = int(soup.find('div', {'class': 'pages'}).find_all('li')[-1].text)

    for page in range(1, pages+1):
        url_page = url + f'&p={page}'

        response_pages = requests.get(url_page)

        soup = BeautifulSoup(response_pages.text, 'html.parser')

        get_block_products = soup.find_all('div', {'class': 'col-lg-4 col-md-4 col-sm-6 col-xs-6'})

        for products in get_block_products:
            description = products.find('div', {'class', 'description-block'})

            if description == None:
                continue

            text_description = description.text.strip('\n')
            
            list_product.append(
                {
                    'Name product': products.find('div', {'class', 'top-block'}).find('div', {'class': 'product-name'}).find('a').text.strip('\n'),
                    'URL product': products.find('div', {'class', 'top-block'}).find('div', {'class': 'product-name'}).find('a').get('href'),
                    'Image product': products.find('div', {'class', 'top-block'}).find('div', {'class': 'product-image'}).find('img').get('data-src'),
                    'Price product': products.find('div', {'class', 'center-block'}).find('div', {'class', 'price-box'}).find('span', {'class': 'price'}).text,
                    'Availability product': products.find('div', {'class', 'center-block'}).find('p', {'class': 'availability'}).text.strip('\n'),
                    'Brief description product': text_description
                }
            )

        with open(PC_PRODUCTS_JSON, 'w') as file:
            json.dump(list_product, file, indent=4, ensure_ascii=False)



if __name__ == '__main__':
    get_response = parser_product('https://www.kiy-v.ua/ua/rozstoechni-shafi.html?dir=asc&order=price')
