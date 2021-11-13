import requests
from bs4 import BeautifulSoup

list_full_href = []

response = requests.get('https://wordsonline.ru')
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

get_div_alphabet_a = soup.find('div', {'class': 'alphabet'}).find_all('a')
# print(get_div_alphabet_a)

for item in get_div_alphabet_a:        
    href = item.get('href')

    if '/' in href:
        full_href = 'https://wordsonline.ru' + href
        # print(full_href)


    response = requests.get(full_href)
    parsing_links = BeautifulSoup(response.text, 'html.parser')

    get_words = parsing_links.find_all('div', {'class': 'col-sm-3 col-xs-6'})
    # print(list_)

    for i in get_words:
        get_ = i.find_all('li')
        # print(get_)

        for n in get_:
            b = n.find('a').text
            print(b)



    
    
