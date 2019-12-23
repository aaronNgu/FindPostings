from bs4 import BeautifulSoup as soup
from URL import make_request

i = 0
var = 1
while var == 1:
    response = make_request(i)
    # pages are marked by post
    response_html = response.read()
    page_soup = soup(response_html, "html.parser")

    #everything is in result info
    list_postings = page_soup.find_all("p", class_="result-info")

    #Assume that every post has a title, price tag, date time and link
    for x in list_postings:
        print(x.find("a", class_="result-title hdrlnk").text)
        print(x.find("a", class_="result-title hdrlnk")['href'])
        print(x.find("span", class_="result-price").text)
        print(x.find("time")['datetime'])
        #Not every post has a housing tag
        print(x.find("span", class_="housing").text)

    postings_done = len(list_postings)
    i += 1

    # exits loop - not 120 postings
    if postings_done <120 :
        print("break")
        break
