import json

from bs4 import BeautifulSoup
import requests

from finder_models import Article

def parser():
    url = 'https://www.obozrevatel.com/search/?q='
    search_url = url + 'авто'
    response = requests.get(search_url).text

    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(str(response))

    with open('index.html', 'r') as file:
        read_file = file.read()

    soup_finder = BeautifulSoup(read_file, 'html.parser')

    find_block_news = soup_finder.find_all('div', {'class': 'newsImgRowTime_inner'})
    # print(find_block_news)

    for news in find_block_news:
        get_text = news.find('a', {'class': 'newsImgRowTime_titleLink'}).text
        get_url = news.find('a', {'class': 'newsImgRowTime_titleLink'}).get('href')

        try:
            a = Article()
            a.text = get_text
            a.url = get_url
            a.save()

        except:
            print('This elemnt is in the database')

get_info = parser()
# print(get_info)
# Article(**get_info).save()


# for n in parsing:
#     print(n)
    
# a = News(inforation = n)
# print(123)
# a.save()