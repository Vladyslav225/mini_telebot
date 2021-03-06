from bs4 import BeautifulSoup
import requests

from finder_models import DataParsing

_dict = {}

def parser(find):

    url = 'https://www.obozrevatel.com/search/?q='
    search_url = url + find
    response = requests.get(search_url).text

    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(str(response))

    with open('index.html', 'r') as file:
        read_file = file.read()

    soup_finder = BeautifulSoup(read_file, 'html.parser')

    find_block_news = soup_finder.find_all('div', {'class': 'newsImgRowTime_inner'})


    for news in find_block_news:
        get_text = news.find('a', {'class': 'newsImgRowTime_titleLink'}).text
        get_url = news.find('a', {'class': 'newsImgRowTime_titleLink'}).get('href')

        _dict['text'] = get_text
        _dict['url'] = get_url
        
        DataParsing(**_dict).save()

