import requests
from bs4 import BeautifulSoup

from mongoengine import *

class BotWords(Document):
    words = StringField(required=True)

url = 'https://wordsonline.ru'

response = requests.get(url)
# print(response)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

get_div_alphabet_a = soup.find('div', {'class': 'alphabet'}).find_all('a')
# print(get_div_alphabet_a)

# Get link words
for item in get_div_alphabet_a:
    # title = item.get('title')
    # print(title)

    href = item.get('href')
    # print(href)

    if '/' in href:
        get_full_url_letter = url + href
        # print(get_full_url_letter)

# Parsing link words
    response = requests.get(get_full_url_letter)
    parsing_url_letter = BeautifulSoup(response.text, 'html.parser')
    # print(parsing_url_letter)

# Get words
    get_div = parsing_url_letter.find_all('div', {'class': 'col-sm-3 col-xs-6'})
    # print(get_div)

    for atribute_li_words in get_div:
        get_atribute_li_words = atribute_li_words.find_all('li')
        # print(get_atribute_li_words)

        for atribute_a in atribute_li_words:
            get_atribute_a = atribute_a.find_all('a')
            # print(get_atribute_a)

            for text_a in get_atribute_a:
                get_text_a = text_a.get_text('a')

                if len(get_text_a) <= 2:
                    continue
                # print(get_text_a)

                connect('db_words_bot_and_users')
                a = BotWords(words=get_text_a)
                a.save()




# url = 'https://wordsonline.ru/%D0%90'

# def get_url(url):
#     response = requests.get(url)
#     return BeautifulSoup(response.text, 'html.parser')


# # print(step_1)

# def get_title_word(title):
#     # print(title)
#     get_title = title.find('h1').text
#     # print(get_title)

#     return get_title

# def get_pages(pagination):
#     get_ = pagination.find('ul', {'class': 'pagination'})
#     print(get_)


# step_1 = get_url(url)
# # print(step_1)

# step_2 = get_title_word(title=step_1)
# # print(step_2)

# step_3 = get_pages(pagination=step_1)
# # print(step_3)





