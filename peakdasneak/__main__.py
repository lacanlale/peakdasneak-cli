from .scraper import Scraper
from .formatter import Formatter
from threading import Timer
from .reddit_scraper import Reddit_Scraper
from .secret import *
import sys
import os


def clr():
        os.system('cls' if os.name=='nt' else 'clear')


def main():
    prmpt = Formatter()
    prmpt.cfg('w', st='b')
    prmpt.out('{:^170}'.format("Welcome to peakdasneak-cli, a tool for assistance with sneaker reselling."))
    reddit = Reddit_Scraper(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, version=0.1)

    prmpt.out("Displaying latest release news collected by Reddit")
    prmpt.out("Date format is: MM/DD/YYYY")
    reddit.scrape(subreddit='sneakers', flair='release', limit=100, sort_by='top', posts_from='week')
    # prmpt.out('{:^170}'.format("Presented is info on StockX for deadstock shoes and the lowest prices on GOAT for the same popular shoes."))
    # scraper = Scraper()
    # shoe_info = scraper.scrape_info()
    # scraper_thread = Timer(500.0, scraper.scrape_info)
    # scraper_thread.start()
    # prmpt.out('Use s to search for a shoes pricing')
    # while True:
    #     action = input(">>> ")
    #     if action == 's':
    #         scraper_thread.cancel()
    #         prmpt.out("Input shoe name")
    #         scraper.search(input(">>> "))

if __name__ == '__main__':
    main()