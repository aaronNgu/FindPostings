import requests
from bs4 import BeautifulSoup as soup

# apt/housing 10km away from V6T1Z4 with 2 bedrooms unfurnished
BASE_URL = 'https://vancouver.craigslist.org/search/'

class Scraper:

    def __init__ (self):
        self.page = ''
        self.postings = {}

    def get(self, link): 
        try:
            response = requests.get(link)
            return response
        except Exception as e : 
            print("Error in get() : {}".format(e))
    
    def url(self, item, **kwargs):
        url = BASE_URL + item + '?'
        for key in kwargs:
            url = url + key + '=' + kwargs[key] + '&'
        return url[:-1]
    
    def parse_postings(self, page):
        list_postings = page_soup.find_all("p", class_="result-info")

    def set_soup(self, page):
        self.page = page

    def set_postings(self, dictionary):
        pass

    def add_postings(self, dictionary):
        pass
        
    def get_postings(self):
        return self.postings

    def get_soup(self):
        return self.soup


if __name__ == '__main__':
    scrapy = Scraper()
    url = scrapy.url('apa', search_distance='10',postal='V6T1Z4')
    response = scrapy.get(url)
    print(response.status_code)