from newspaper import Article
import requests
from bs4 import BeautifulSoup


def get_post_links():
    html_doc = requests.get('http://kachamukabe.com').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    article_list = soup('h1')
    titles = []
    for h1 in article_list:
        for link in h1.find_all('a'):
            titles.append(get_post_data(link.get('href'))+'\n'+link.get('href'))
    return titles


def get_post_data(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title


get_post_links()
