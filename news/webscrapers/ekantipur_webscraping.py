import requests
from bs4 import BeautifulSoup

website_url = "https://ekantipur.com"


def ekantipur_detail_webscraping(link):
    url = website_url + link
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    description = soup.find('div', class_='description').text
    return description


def ekantipur_list_webscraping():
    url = website_url + "/news"
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = soup.find_all('article')
    list_of_scrapped_articles = []
    for article in articles:
        title = article.find('a').text
        image = article.find('img').get('data-src')
        source = 'ekantipur'
        link = article.find('a').get('href')
        description = ekantipur_detail_webscraping(link)
        list_of_scrapped_articles.append([title, image, source, description])

    return list_of_scrapped_articles


