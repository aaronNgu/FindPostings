import requests
from bs4 import BeautifulSoup as soup
from parser import Parser

# apt/housing 10km away from V6T1Z4 with 2 bedrooms unfurnished
BASE_URL = 'https://vancouver.craigslist.org/search/'

class Scraper:

    def __init__ (self):
        self.page = ''
        self.postings = {}
        self.parse = Parser()

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
    
    def parse_single_page_postings(self, page):
        list_postings = page.find_all("p", class_="result-info")

        result = []
        #Assume that every post has a title, price tag, date time and link
        for x in list_postings:
            single_post = {}
            title = x.find("a", class_="result-title hdrlnk").text
            link = x.find("a", class_="result-title hdrlnk")['href']
            price = x.find("span", class_="result-price").text
            time = x.find("time")['datetime']
            numberOfBedroom = x.find("span", class_="housing") 
            numberOfBedroom = numberOfBedroom if numberOfBedroom == None else numberOfBedroom.text
            single_post['title'] = title
            single_post['link'] = link
            single_post['price'] = self.parse.parse_price(price)
            single_post['date'] = self.parse.parse_datetime(time)[0]
            single_post['time'] = self.parse.parse_datetime(time)[1]
            single_post['numberOfBedroom'] = numberOfBedroom
            result.append(single_post)

        return result
    
    def get_all_postings_for_item(self, item, **kwargs):
        pass

    def find_how_many_postings(self, page):
        return page.find("span", class_="totalcount").text

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