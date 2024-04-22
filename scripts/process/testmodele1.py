import requests
#import urllib.request
from bs4 import BeautifulSoup as soup



tout = []
url = 'https://www.yelp.com/biz/surisan-san-francisco'
html = requests.get(url)
#print(html)
comms = soup(html.text, 'html.parser')
#print (comms)

articles = comms.find_all("div", class_=" css-1qn0b6x")
print (articles)

for article in articles :
    reviews = article.find("span", lang="en")
    clean_reviews = [review.get_text().strip() for review in reviews]

print(clean_reviews)

