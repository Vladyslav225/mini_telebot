import json

from bs4 import BeautifulSoup
import requests

list_news = []

def parser(url):
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # # print(soup)

    # finder = url + 'авто'
    # # print(finder)

    # response_finder = requests.get(finder).text
    # # print(response_finder)

    # with open('index.html', 'w', encoding='utf-8') as file:
    #     file.write(str(response_finder))

    with open('index.html', 'r') as file:
        read_file = file.read()

    soup_finder = BeautifulSoup(read_file, 'html.parser')

    find_block_news = soup_finder.find_all('div', {'class': 'newsImgRowTime_inner'})
    # print(find_block_news)

    for news in find_block_news:
        list_news.append(
            {
                "Name news": news.find('a', {'class': 'newsImgRowTime_titleLink'}).text,
                "URL news": news.find('a', {'class': 'newsImgRowTime_titleLink'}).get('href')
            }
        )
    return list_news


parsing = parser('https://www.obozrevatel.com/search/?q=')
print(parsing)