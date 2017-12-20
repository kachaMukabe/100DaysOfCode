import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://www.google.com/'


def search_g_images(query):
    query = query.replace(' ', '+')
    search_query = 'search?q='+query+'&source=lnms&tbm=isch'
    html_doc = requests.get(BASE_URL+search_query).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.find_all('a', class_=''))


search_g_images('steven universe')
