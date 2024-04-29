import requests
#import urllib.request
from bs4 import BeautifulSoup as soup

headers = {
        'User-Agent': 'Googlebot',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',  # Do Not Track Request Header
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }

#proxies = {"http":"159.65.245.255", "https" : "159.65.245.255"}

tout = []
url = 'https://www.yelp.com/biz/surisan-san-francisco'
html = requests.get(url, headers = headers)
#print(html)
comms = soup(html.text, 'html.parser')
#print (comms)

articles = comms.find_all("div")
print (articles)

""" for article in articles :
    reviews = article.find("span", lang="en")
    clean_reviews = [review.get_text().strip() for review in reviews]

    print(clean_reviews) """

