import requests
from bs4 import BeautifulSoup as soup

def find_pages(url_base):
    
    page = 0
    lien = []
    while True:
        url = f"https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&start={page * 10}"
        html = requests.get(url)
        #print(response.status_code)  
        resto = soup(html.text, 'html.parser')

        articles = resto.find_all("li", class_="css-1qn0b6x")  
        for article in articles:
            links = article.find_all("a")
            for link in links:
                if link['href'].startswith("/biz/") :
                    lien.append(url_base + link['href'])

        if not articles:
            break
        page += 1
    return lien

def find_comms_stars (lst):
    for url in lst :
        html = requests.get(url)
        #print(response.status_code)  
        resto = soup(html.text, 'html.parser')
        reviews = resto.find_all("span", lang="en")
        print (reviews)


def main () :
    """headers = {
         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0)Gecko/20100101 Firefox/104.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',  # Do Not Track Request Header
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    } """
    url_base = 'https://www.yelp.com'

    lst_liens = find_pages(url_base)
    find_comms_stars(lst_liens)

main()
