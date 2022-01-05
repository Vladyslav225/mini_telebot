from bs4 import BeautifulSoup
import requests

from finder_models import DataParsing
# from finder_connector import parsing_answer_save_db

_dict = {}

def parser(find):

    print('parser')

    url = 'https://www.obozrevatel.com/search/?q='
    search_url = url + find
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

        _dict['text'] = get_text
        _dict['url'] = get_url

    # parsing_answer_save_db(**_dict)
        DataParsing(**_dict).save()

