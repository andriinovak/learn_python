from urllib.request import urlretrieve
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from requests import get
import csv

class Overclockers:
    url_site = 'https://overclockers.ua'

    def get_page(self):
        over_page_get = get(Overclockers.url_site)
        self.page_text = BeautifulSoup(over_page_get.text, features="html.parser")

    def get_links_reviews(self):
        last_reviews = self.page_text.find_all('div', 'review')
        list_with_links = []
        for line in last_reviews:
            a = line.find('a')
            full_url = urljoin(Overclockers.url_site, a.attrs['href'])
            headline = a.img.attrs['alt']
            list_with_links.append((headline, full_url))
        return set(list_with_links)

    def get_pictures_from_reviews(self):
        links = self.get_links_reviews()
        list_with_links_on_pictures = []
        for link in links:
            list_with_links_on_pictures.append(self.get_article_pictures(link))
        return list_with_links_on_pictures

    def get_article_pictures(self, link):
        page_text = get(link)
        page_text = BeautifulSoup(page_text.text, features="html.parser")
        find_id_article = page_text.find(id='article')
        find_link_on_picture = find_id_article.find_all('img')
        list_with_pictures = []
        for item in find_link_on_picture:
            full_url = urljoin(Overclockers.url_site, item.attrs['src'])
            list_with_pictures.append(full_url)
        return list_with_pictures

    def save_pictures_to_files(self, picture_list):
        for item in picture_list:
            name_file = item.split('/')[-1]
            urlretrieve(item, name_file)
            print(f'file save {name_file}')


our_page = Overclockers()
our_page.get_page()
# pprint(our_page.get_links_reviews())
# for item in our_page.get_pictures_from_reviews():
#     our_page.save_pictures_to_files(item)
list_with_headlines = our_page.get_links_reviews()
text = 'heading,link'

with open('new_file.csv', mode='w', encoding='UTF8', newline='') as f:
    file_writer = csv.writer(f)
    file_writer.writerow(['heading', 'link'])
    for item in list_with_headlines:
        header, link = item
        header = header.replace('.', ',')
        file_writer.writerow((header, link))
