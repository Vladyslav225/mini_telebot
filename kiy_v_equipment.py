# All type equipment

import requests
from bs4 import BeautifulSoup
import json


equipment_categories_list = []

thermal_equipment_categ_list = []
oven_combi_oven_list = []
oven_combi_prod_info = []


EQUIPMENT_PAGE_HTML = 'kiy_v_html/equipment_page.html'
EQUIPMENT_CATEGORIES = 'kiy_v_json/equipment_categories.json'

EQUIPMENT_THERMAL_PAGE_HTML = 'kiy_v_html/equipment_thermal_page.html'
EQUIP_THERMAL_CATEGORIES = 'kiy_v_json/equip_thermal_categories.json'

EQUIPMENT_OVEN_COMBI_OVEN_HTML = 'kiy_v_html/equip_oven_combi_oven.html'
EQUIP_OVEN_COMBI_OVEN = 'kiy_v_json/equip_oven_combi_oven_categories.json'

EQUIP_COMBI_OVEN_HTML = 'kiy_v_html/equip_combi_oven.html'
EQUIP_COMBI_OVEN = 'kiy_v_json/equip_combi_oven_categories.json'



def equipment_page(url):
    res_equipment_page = requests.get(url).text

    with open(EQUIPMENT_PAGE_HTML, 'w') as file:
        file.write(str(res_equipment_page))

def equipment_categories():
    with open(EQUIPMENT_PAGE_HTML, 'r') as file:
        src = file.read()

    soup_equip_categories = BeautifulSoup(src, 'html.parser')

    get_general_class_categ = soup_equip_categories.find_all('div', {'class': 'grid-item normal category'})

    for all_equipment_categories in get_general_class_categ:
        equipment_categories_list.append(
            {
                'Name category': all_equipment_categories.find('a').find('span').text,
                'URL category': all_equipment_categories.find('a').get('href'),
                'Image category': all_equipment_categories.find('a').find('img').get('data-src')
            }
        )

    with open(EQUIPMENT_CATEGORIES, 'w') as file:
        json.dump(equipment_categories_list, file, indent=4, ensure_ascii=False)

    # print(equipment_categories_list)

def thermal_eqipment_page():
    with open(EQUIPMENT_CATEGORIES) as file:
        categories = json.load(file)
        url_category = categories[0]['URL category']
        # print(url_category)

    res_thermal_eqipment = requests.get(url_category).text

    with open(EQUIPMENT_THERMAL_PAGE_HTML, 'w') as file:
        file.write(str(res_thermal_eqipment))

def thermal_eqipment_categories():
    with open(EQUIPMENT_THERMAL_PAGE_HTML, 'r') as file:
        src = file.read()

    soup_thermal_eqipment_cat = BeautifulSoup(src, 'html.parser')

    get_general_class_thermal = soup_thermal_eqipment_cat.find_all('div', {'class': 'grid-item normal category'})

    for all_thermal_eqipment_categ in get_general_class_thermal:
        thermal_equipment_categ_list.append(
            {
                'Name category': all_thermal_eqipment_categ.find('a').find('span').text,
                'URL category': all_thermal_eqipment_categ.find('a').get('href'),
                'Image category': all_thermal_eqipment_categ.find('a').find('img').get('data-src')
            }
        )
    
    with open(EQUIP_THERMAL_CATEGORIES, 'w') as file:
        json.dump(thermal_equipment_categ_list, file, indent=4, ensure_ascii=False)

def page_oven_combi_oven():
    with open(EQUIP_THERMAL_CATEGORIES) as file:
        categ_thermal_eqipment = json.load(file)

    url_oven_combi_oven = categ_thermal_eqipment[0]['URL category']
    # print(url_oven_combi_oven)

    res_oven_combi_oven = requests.get(url_oven_combi_oven).text

    with open(EQUIPMENT_OVEN_COMBI_OVEN_HTML, 'w') as file:
        file.write(str(res_oven_combi_oven))

def oven_combi_oven_categories():
    with open(EQUIPMENT_OVEN_COMBI_OVEN_HTML, 'r') as file:
        page_oven_combi_oven = file.read()

    soup_oven_combi_oven = BeautifulSoup(page_oven_combi_oven, 'html.parser')

    get_general_class_oven_combi_oven = soup_oven_combi_oven.find_all('div', {'class': 'grid-item normal category'})

    for all_oven_combi_oven  in get_general_class_oven_combi_oven:
        oven_combi_oven_list.append(
            {
                'Name category': all_oven_combi_oven.find('a').find('span').text,
                'URL category': all_oven_combi_oven.find('a').get('href'),
                'Image category': all_oven_combi_oven.find('a').find('img').get('data-src')
            }
        )
    # print(oven_combi_oven_list)

    with open(EQUIP_OVEN_COMBI_OVEN, 'w') as file:
        json.dump(oven_combi_oven_list, file, indent=4, ensure_ascii=False)

def combi_ovens_page():
    with open(EQUIP_OVEN_COMBI_OVEN) as file:
        combi_ovens = json.load(file)

    url_combi_ovens = combi_ovens[0]['URL category']
    # print(url_combi_ovens)

    res_combi_ovens = requests.get(url_combi_ovens).text
    print(res_combi_ovens)

    with open(EQUIP_COMBI_OVEN_HTML, 'w') as file:
        file.write(str(res_combi_ovens))

def products_combi_oven():
    with open(EQUIP_COMBI_OVEN_HTML, 'r') as file:
        product = file.read()

    soup_product = BeautifulSoup(product, 'html.parser')

    general_class_products = soup_product.find_all('div', {'class': 'col-lg-4 col-md-4 col-sm-6 col-xs-6'})

    for product_info in general_class_products:
        oven_combi_prod_info.append(
            {
                'Name product': product_info.find('div', {'class': 'top-block'}).find('div', {'class': 'product-name'}).find('a').text.strip('\n'),
                'URL product': product_info.find('a').get('href'),
                'Image product': product_info.find('div', {'class': 'product-image'}).find('a').find('img').get('data-src'),
                'Price product': product_info.find('div', {'class': 'center-block'}).find('div', {'class': 'price-box'}).find('span', {'class': 'price'}).text,
                'Brief description product': product_info.find('div', {'class': 'description-block'}).text
            }
        )

    # print(oven_combi_prod_info)
    with open(EQUIP_COMBI_OVEN, 'w') as file:
        json.dump(oven_combi_prod_info, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    get_url_basic_page = equipment_page('https://www.kiy-v.ua/ua/oborudovanie.html')
    get_url_equipment = equipment_categories()

    get_thermal_eqipment_page = thermal_eqipment_page()
    get_thermal_eqipment_categories = thermal_eqipment_categories()

    get_oven_combi_oven_page = page_oven_combi_oven()
    get_oven_combi_oven_categories = oven_combi_oven_categories()

    get_combi_ovens_page = combi_ovens_page()
    get_products_combi_oven = products_combi_oven()
