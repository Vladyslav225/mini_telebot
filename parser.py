import requests
from bs4 import BeautifulSoup

start_page = 'https://wordsonline.ru'

def get_start_page(start_page):
    try:
        response = requests.get(start_page)
    except:
        print('123')

    return BeautifulSoup(response.text, 'html.parser')

def get_urls(objects):
    dict_href = {}

    try:
        get_div_alphabet_a = objects.find('div', {'class': 'alphabet'}).find_all('a')
        # print(get_div_alphabet)
        
    except:
        print('I can not find this element')

    for item in get_div_alphabet_a:        
        href = item.get('href')
        # print(href)

        # get_text_title = item.get('title')
        # print(get_text_title)

        if '/' in href:
            full_href = 'https://wordsonline.ru' + href
        # print(full_href)

    # dict_href['href'] = full_href

            return full_href
        
# def parsing_urls(urls, ):
#     response = requests.get(urls)
#     print(response)





start_page = 'https://wordsonline.ru'

basic_page = get_start_page(start_page)
# print(basic_page)

all_urls = get_urls(objects=basic_page)
print(all_urls)
# n = all_urls

# collection_from_urls = parsing_urls(urls=all_urls)
# print(collection_from_urls)

# response1 = requests.get(n)
# print(response1)


