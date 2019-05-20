from .formatter import Formatter
from bs4 import BeautifulSoup
import requests

class Scraper:
    err = Formatter()
    notif = Formatter()
    cash = Formatter()
    err.cfg('r', st='b')
    notif.cfg('c', st='i')
    cash.cfg('g', st='u')

    def __init__(self, url, cfg):
        self.url = url
        self.cfg = cfg

    def scrape_info(self):
        resp = requests.get(self.url)
        if(resp.status_code != 200):
            self.err.out(f"[Invalid status code: {resp.status_code};  unable to connnect to {self.url}]")
            exit()
        soup = BeautifulSoup(resp.text, 'lxml')
        if self.cfg == "stockx":
            self.notif.out("Now printing the most recent lowest price for popular shoes")
            popular_items = soup.find_all('div', attrs={'class', 'tile browse-tile'})
            for item in popular_items:
                shoe_name = item.find('div', attrs={'class':'PrimaryText-sc-12c6bzb-0 gMymmc'}).text
                shoe_price = item.find('div', attrs={'class':'PrimaryText-sc-12c6bzb-0 jwzdVc'}).text
                print(f"{shoe_name}: ", end='')
                self.cash.out(f"{shoe_price}")