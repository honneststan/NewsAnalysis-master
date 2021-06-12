import requests
from bs4 import BeautifulSoup

website_url = "https://www.onlinekhabar.com"


def onlinekhabar_detail_webscraping(link):
    url = link
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    description = soup.find('div', class_='col colspan3 main__read--content ok18-single-post-content-wrap').text
    return description


def onlinekhabar_list_webscraping():
    url = website_url + "/content/news"
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = soup.find_all('div', class_='relative list__post show_grid--view')
    list_of_scrapped_articles = []
    for article in articles:
        title = article.find('div', class_='item__wrap').find('a').text
        image = article.find('img').get('src')
        source = 'onlinekhabar'
        link = article.find('a').get('href')
        description = onlinekhabar_detail_webscraping(link)
        list_of_scrapped_articles.append([title, image, source, description])

    return list_of_scrapped_articles


