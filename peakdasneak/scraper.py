from .formatter import Formatter
from bs4 import BeautifulSoup
import requests
import os
import time

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

    def __clr(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def scrape_info(self):
        if self.cfg == "stockx":
            stockX = Formatter()
            stockX.cfg('g', st='b')
            shoes = {}
            while True:
                resp = requests.get(self.url)
                if(resp.status_code != 200):
                    self.err.out(f"[Invalid status code: {resp.status_code};  unable to connnect to {self.url}]")
                    exit()
                soup = BeautifulSoup(resp.text, 'lxml')

                stockX.out("   _____ _             _    __   __ ")
                stockX.out("  / ____| |           | |   \ \ / / ")
                stockX.out(" | (___ | |_ ___   ___| | __ \ V /  ")
                stockX.out("  \___ \| __/ _ \ / __| |/ /  > <   ")
                stockX.out("  ____) | || (_) | (__|   <  / . \  ")
                stockX.out(" |_____/ \__\___/ \___|_|\_\/_/ \_\ ")
                stockX.out("                                    ")
                self.notif.out("Now displaying the most recent, lowest price for popular shoes")
                self.notif.out("Updating prices every 5 minutes")

                popular_items = soup.find_all('div', attrs={'class', 'tile browse-tile'})
                for item in popular_items:
                    shoe_name = item.find('div', attrs={'class':'PrimaryText-sc-12c6bzb-0 gMymmc'}).text
                    shoe_price = item.find('div', attrs={'class':'PrimaryText-sc-12c6bzb-0 jwzdVc'}).text
                    if shoe_name in shoes:
                        prev_price = int(shoes[shoe_name][1:])
                        curr_price = int(shoe_price[1:])
                        diff = abs(prev_price - curr_price)
                        if prev_price < curr_price:
                            shoes[shoe_name] = f"{shoe_price} up ${diff}"
                        elif prev_price > curr_price:
                            shoes[shoe_name] = f"{shoe_price} down ${diff}"
                        else:
                            shoes[shoe_name] = f"{shoe_price} unchanged"
                    else:
                        shoes[shoe_name] = shoe_price
                        
                for shoe_name, shoe_price in shoes.items():
                    print(f"{shoe_name}: ", end='')
                    self.cash.out(f"{shoe_price}")
                
                time.sleep(500)
                self.__clr()