from .scraper import Scraper
from .formatter import Formatter
from threading import Timer
import sys
import os


def main():
    prmpt = Formatter()
    prmpt.cfg('w', st='b')
    prmpt.out('{:^170}'.format("Welcome to peakdasneak-cli, a tool for the assistance with sneaker reselling."))
    prmpt.out('{:^170}'.format("Presented is info on StockX for deadstock shoes and the lowest prices on GOAT for the same popular shoes."))
    scraper = Scraper()
    shoe_info = scraper.scrape_info()
    scraper_thread = Timer(500.0, scraper.scrape_info, shoe_info)
    scraper_thread.start()
    prmpt.out('Use s to search for a shoes pricing')
    while True:
        action = input(">>> ")
        if action == 's':
            scraper_thread.cancel()
            prmpt.out("Input shoe name")
            scraper.search(input(">>> "))


if __name__ == '__main__':
    main()