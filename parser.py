import requests
from bs4 import BeautifulSoup

dict_words = {}

url = 'https://wordsonline.ru'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

get_div_alphabet_a = soup.find('div', {'class': 'alphabet'}).find_all('a')
# print(get_div_alphabet_a)

# Get link words
for item in get_div_alphabet_a:
    title = item.get('title')
    print(title)

    href = item.get('href')

    if '/' in href:
        get_full_url_letter = url + href
        # print(get_full_url_letter)

# Parsing link words
    response = requests.get(get_full_url_letter)
    parsing_url_letter = BeautifulSoup(response.text, 'html.parser')

# Get words
    get_div = parsing_url_letter.find_all('div', {'class': 'col-sm-3 col-xs-6'})
    # print(get_div)

    for atribute_li_words in get_div:
        get_atribute_li_words = atribute_li_words.find_all('li')
        # print(get_)

        for atribute_a in atribute_li_words:
            get_atribute_a = atribute_a.find_all('a')
            # print(get_words)

            for text_a in get_atribute_a:
                get_text_a = text_a.get_text('a')
                print(get_text_a)


        
