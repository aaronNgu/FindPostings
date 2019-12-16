import requests
from bs4 import BeautifulSoup as soup
from parser import Parser

# apt/housing 10km away from V6T1Z4 with 2 bedrooms unfurnished
BASE_URL = 'https://vancouver.craigslist.org/search/'

class Scraper:

    def __init__ (self):
        self.page = ''
        self.postings = []
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

            #setting values
            single_post['title'] = title
            single_post['link'] = link
            single_post['price'] = self.parse.parse_price(price)
            datetime = self.parse.parse_datetime(time)
            single_post['date'] = datetime[0]
            single_post['time'] = datetime[1]
            bedrooms_squarefoot = self.parse.parse_numberOfBedroom(numberOfBedroom)
            single_post['bedroom'] = bedrooms_squarefoot[0]
            single_post['squareFoot'] =  bedrooms_squarefoot[1]
            result.append(single_post)

        return result
    
    def get_parse_and_add_single_page(self, url):
        response = self.get(url)
        page = soup(response.content, 'html.parser')
        self.set_page(page)
        lists = self.parse_single_page_postings(self.get_page())
        self.add_postings(lists)

        return len(lists)

    def get_all_postings_for_item(self, item, **kwargs):
        #assume each page has 120 postings
        url = self.url(item, **kwargs)
        self.get_parse_and_add_single_page(url)

        total_postings = self.find_how_many_postings(self.get_page())
        #first page retrieves 120 postings
        postings_seen = 120
        
        while(postings_seen < int(total_postings)):
            url = self.url(item, **kwargs, s=str(postings_seen))
            seen = self.get_parse_and_add_single_page(url)
            postings_seen += seen

    def find_how_many_postings(self, page):
        return page.find("span", class_="totalcount").text

    def set_page(self, page):
        self.page = page

    def add_postings(self, new_lists):
        self.postings += new_lists
        
    def get_postings(self):
        return self.postings

    def get_page(self):
        return self.page


if __name__ == '__main__':
    scrapy = Scraper()
    url = scrapy.url('apa', search_distance='10',postal='V6T1Z4')
    response = scrapy.get(url)
    print(response.status_code)