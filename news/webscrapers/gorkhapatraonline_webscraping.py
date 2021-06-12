import requests
from bs4 import BeautifulSoup

website_url = "https://gorkhapatraonline.com/mainnews"


def gorkhapatraonline_detail_webscraping(link):
    url = link
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    description = soup.find('div', class_='newstext').text
    return description


def gorkhapatraonline_list_webscraping():
    url = website_url
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = soup.find_all('div', class_='business')
    list_of_scrapped_articles = []
    for article in articles:
        title = article.find('p', class_="trand middle-font").text
        image = article.find('img').get('src')
        source = 'gorkhapatraonline'
        link = article.find('a').get('href')
        description = gorkhapatraonline_detail_webscraping(link)
        list_of_scrapped_articles.append([title, image, source, description])

    return list_of_scrapped_articles


