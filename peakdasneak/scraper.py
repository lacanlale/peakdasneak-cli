from .formatter import Formatter
from bs4 import BeautifulSoup
import requests
import os
import time

stockX = """
      _____ _             _    __   __
     / ____| |           | |   \ \ / /
    | (___ | |_ ___   ___| | __ \ V / 
     \___ \| __/ _ \ / __| |/ /  > <  
     ____) | || (_) | (__|   <  / . \ 
    |_____/ \__\___/ \___|_|\_\/_/ \_\\
"""

goat = """
"""
class Scraper:
    err = Formatter()
    notif = Formatter()
    cash = Formatter()
    prmpt = Formatter()
    prmpt.cfg('w', st='b')
    err.cfg('r', st='b')
    notif.cfg('c', st='i')
    cash.cfg('g', st='u')

    stockx_url = 'https://stockx.com/sneakers/most-popular'
    stockx_search = 'https://stockx.com/search?s='

    goat_url = 'https://www.goat.com/sneakers'
    goat_search = 'https://www.goat.com/search?query='

    def __clr(self, shoes):
        os.system('cls' if os.name=='nt' else 'clear')

    def scrape_info(self, shoes={'stockx' : {}, 'goat' : {}}):
        banner = Formatter()
        banner.cfg('g', st='b')
        banner.out(f"{stockX}")
        resp = requests.get(self.stockx_url)
        if(resp.status_code != 200):
            self.err.out(f"[Invalid status code: {resp.status_code};  unable to connnect to {self.url}]")
            exit()
        soup = BeautifulSoup(resp.text, 'lxml')

        self.notif.out("Now displaying the most recent, lowest price for popular shoes")
        self.notif.out("Updating prices every 5 minutes")

        popular_items = soup.find_all('div', attrs={'class', 'tile browse-tile'})
        for item in popular_items:
            shoe_name = item.find('div', attrs={'class':'PrimaryText-sc-12c6bzb-0 gMymmc'}).text
            shoe_price = item.find('div', attrs={'class':'PrimaryText-sc-12c6bzb-0 jwzdVc'}).text
            if shoe_name in shoes:
                prev_price = int(shoes['stockx'][shoe_name].split(' ')[0][1:])
                curr_price = int(shoe_price[1:])
                diff = abs(prev_price - curr_price)
                if prev_price < curr_price:
                    shoes['stockx'][shoe_name] = f"{shoe_price} up ${diff}"
                elif prev_price > curr_price:
                    shoes['stockx'][shoe_name] = f"{shoe_price} down ${diff}"
                else:
                    shoes['stockx'][shoe_name] = f"{shoe_price}"
            else:
                shoes['stockx'][shoe_name] = shoe_price
        
        counter = 0
        for shoe_name, shoe_price in shoes['stockx'].items():
            print(f"{counter}.) {shoe_name}: ", end='')
            shoe_price_split = shoe_price.split(" ")
            if len(shoe_price_split) > 1:
                print(f"${shoe_price_split[0]} ", end='')
                if shoe_price_split[1] == 'up':
                    print(f"\033[92m{shoe_price_split[1]} ${shoe_price_split[2]}\033[00m")
                else:
                    print(f"\033[91m{shoe_price_split[1]} ${shoe_price_split[2]}\033[00m")
            else:
                self.cash.out(f"{shoe_price}")
            counter += 1

        return shoes
    
    def search(self, shoe_name):
        name = shoe_name.replace(" ", "%20").lower()
        
        resp = requests.get(f"{stockX}{name}")