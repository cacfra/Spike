import requests

from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def main():
    #https://coinmarketcap.com/all/views/all
    all_links = []

if __name__ == '__main__':
    main()
# COMMENT
