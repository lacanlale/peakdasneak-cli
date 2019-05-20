from .scraper import Scraper
import sys


def main():
    stockx = Scraper('https://stockx.com/sneakers/most-popular', 'stockx')
    stockx.scrape_info()


if __name__ == '__main__':
    main()