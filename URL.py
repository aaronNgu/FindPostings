from urllib.request import urlopen

# apt/housing 10km away from V6T1Z4 with 2 bedrooms unfurnished
base = "https://vancouver.craigslist.org/search/apa?"
distance = "search_distance=10"
location = "postal=V6T1Z4"
number_Bedroom = "min_bedrooms=2&max_bedrooms=2"
#0 - all time, 1 - within 30days, 2 - beyond 30 days
timeframe = "availabilityMode=1"
openHouseDate = "sale_date=all+dates"
furnished = "is_furnished=0"
#starting posts - zero indexed
page = "s="


URL = base + "&" + distance + "&" + location + "&" + number_Bedroom + "&" + timeframe + "&" + furnished + "&"+ openHouseDate + "&"+ page

def make_request(number):
    page_number = str(120*number)
    response = urlopen(URL + page_number)

    if(response.status == 200):
        print("Request successful")
    else:
        print("error code :" + str(response.status))

    return response

#SABJ6-N8QBK-74N2C-YZ4K9-QJ3QV
