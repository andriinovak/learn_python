from bs4 import BeautifulSoup
from requests import get


URL = 'https://www.overclockers.ua/'


def get_text_from_url(url):
    