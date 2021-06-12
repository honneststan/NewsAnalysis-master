import requests
from bs4 import BeautifulSoup

website_url = "https://baahrakhari.com/"


def baahrakhari_detail_webscraping(link):
    url = link
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    description = soup.find('div', class_='detail-box').text
    return description


def baahrakhari_list_webscraping():
    url = website_url
    r = requests.get(url)
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = soup.find_all('div', class_="news-break breaking-normal")
    list_of_scrapped_articles = []
    for article in articles:
        title = article.find('span', class_="main-title").text
        image = article.find('img').get('src')
        image = image.replace(' ', '%20')
        source = 'baahrakhari'
        link = article.find('a').get('href')
        description = baahrakhari_detail_webscraping(link)
        list_of_scrapped_articles.append([title, image, source, description])

    return list_of_scrapped_articles

