from .scraper import Scraper
from .formatter import Formatter
from threading import Timer
from .reddit_scraper import Reddit_Scraper
from .secret import *
from webbrowser import open as wbopen
import sys
import os

prmpt = Formatter()
prmpt.cfg('w', st='b')

def clr():
        os.system('cls' if os.name=='nt' else 'clear')


def disp_goatx():
    prmpt.out("Presented is info on StockX for deadstock shoes and the lowest prices on GOAT for the same popular shoes.")
    scraper = Scraper()
    shoe_info = scraper.scrape_info()
    scraper_thread = Timer(500.0, scraper.scrape_info)
    scraper_thread.start()
    prmpt.out('Use s to search for a shoes pricing')
    while True:
        action = input(">>> ")
        if action == 's':
            scraper_thread.cancel()
            prmpt.out("Input shoe name")
            scraper.search(input(">>> "))


def disp_reddit():
    reddit = Reddit_Scraper(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, version=0.1)
    prmpt.out("Displaying latest release news collected by Reddit")
    prmpt.out("Date format is: MM/DD/YYYY")
    urls = reddit.scrape(subreddit='sneakers', flair='release', limit=500, sort_by='top', posts_from='month')
    prmpt.out("Enter the number of the post to open || Enter e to exit to main menu")
    inp = input(">>> ")
    
    while not inp in urls and not inp == 'e':
        inp = input(">>> ")
    
    if inp == 'e':
        clr()
        disp_main()
        return

    wbopen(urls[inp])
    disp_reddit()


def disp_main():
    prmpt.out('{:^170}'.format("Welcome to peakdasneak-cli, a tool for assistance with sneaker reselling."))
    prmpt.out('{:^170}'.format("Select a display option"))
    prmpt.out('1.) Display Reddit data on new releases')
    prmpt.out('2.) Display Goat+StockX data on trending shoes')
    prmpt.out('3.) Exit')
    inp = input(">>> ")
    
    while not inp == '1' and not inp == '2' and not inp == '3':
        inp = input(">>> ")

    return inp


def main():
    opt = disp_main()
    if opt == '1':
        disp_reddit()
    elif opt == '2':
        disp_goatx()
    else:
        exit()

if __name__ == '__main__':
    main()