from .scraper import Scraper
from .formatter import Formatter
import sys
import os


def main():
    prmpt = Formatter()
    prmpt.cfg('w', st='b')
    prmpt.out('{:^170}'.format("Welcome to peakdasneak-cli, a tool for the assistance with sneaker reselling."))
    prmpt.out('{:^170}'.format("Presented is info on StockX for deadstock shoes and the lowest prices on GOAT for the same popular shoes."))
    stockx = Scraper('https://stockx.com/sneakers/most-popular', 'stockx')
    stockx.scrape_info()


if __name__ == '__main__':
    main()