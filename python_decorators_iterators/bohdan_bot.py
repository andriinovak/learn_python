import sys
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from requests import get
import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(asctime)s: %(name)s - %(levelname)s - %(message)s')
logging.debug('This will get logged')
PIRAMIDA_URL = 'http://www.piramida.rv.ua'


class Converter:

    def __init__(self, url):
        self.log = logging.getLogger('Converter')
        self.url = url
        self.kurs_table = self.__get_kurs()
        self.kurs_dict = self.parse_table_kurs()

    def __get_kurs(self):
        try:
            raise ZeroDivisionError("hello zero divizion")
            piramida_kurs = get(self.url)
            self.log.info('getting value from piramida')
            soup = BeautifulSoup(piramida_kurs.text, features="html.parser")
            table_with_kurs = soup.find(id='maintb')
            return table_with_kurs
        except RequestException as ex:
            eror = f'Error getting url: {ex}'
            self.log.error(eror)
        except Exception as excep:
            self.log.exception(f'you get error {excep}')
            sys.exit(eror)

    def parse_table_kurs(self):
        tbody = self.kurs_table.tbody
        tbody_list = tbody.find_all('tr')
        dict_with_text = {}
        for item in tbody_list:
            item_tds = item.find_all('td')
            dict_with_text[item_tds[0].text] = {'buy': float(item_tds[1].text), 'sell': float(item_tds[2].text)}
        return dict_with_text

    def convert(self, money, name_operation, value):
        return self.kurs_dict[money][name_operation] * float(value)


money = Converter('')
print(money.convert('USD', 'sell', 100))
