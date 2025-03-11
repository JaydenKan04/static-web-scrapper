#!/usr/bin/env python

import xlsxwriter
import requests
from bs4 import BeautifulSoup

def getAllItems(HTMLParser):
    items = html_parser.find_all('div', class_='col-md-4 col-xl-4 col-lg-4')


def getHtmlParser(path):
    url = 'https://webscraper.io/test-sites/e-commerce/allinone' + path
    r = requests.get(url)

    if(r.status_code != 200):
        print("ERROR : Can't establish connection at " + url)
        return

    print("Succesfully establish connection at" + url)
    html_parser = BeautifulSoup(r.content, 'html.parser')
        
    return html_parser

def main():
    print("Hello")

    paths = ['/computers/laptops', '/computers/tablets', '/phones/touch']
    for path in paths:
        print(getHtmlParser(path))

if __name__ == "__main__":
    main()