itesmport requests
from bs4 import BeautifulSoup as soup
from time import sleep
import csv

def find_pages(url_base, headers):
    
    page = 0
    lien = []
    while page <=10:
        url = f"{url_base}/s?k=books&page={page}"
        html = requests.get(url, headers=headers)
        #print(response.status_code)  
        livres = soup(html.text, 'html.parser')

        articles = livres.find_all("span", class_="a-declarative")  
        for article in articles:
            links = article.find_all("a")
            for link in links:
                lien.append(url_base + link['href'])

        if not articles:
            break
        page += 1
        sleep(2)
    return lien

def find_comms (lst, headers):
    tout=[]
    for url in lst :
        html = requests.get(url, headers=headers)
        #print(response.status_code)  
        comms = soup(html.text, 'html.parser')
        #print(comms)
        comments = comms.find_all('span', {'class': 'a-size-base review-text review-text-content'})
    ratings = comms.find_all('span', {'class': 'a-icon-alt'})
    id = comms.find_all('span', {'class': 'a-profile-name'})

    for i in range (0, len(comments)):
        tout.append({"Identifiant" : id[i],
                    "Commentaire" : comments[i],
                    "Note" : int(ratings[i]),
                    "Note_str" : ratings[i]
                    })
    return tout


def to_csv (tout) :
    titres = ['id', 'text', 'label', 'label_text']

    with open('dataset.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=titres)
        writer.writeheader()

        for row in tout:
            writer.writerow(row)

def main():
    url_base = "https://www.amazon.fr"
    results = []
    headers = {
         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0)Gecko/20100101 Firefox/104.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1', 
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    lst = find_pages(url_base, headers)
    page_results = find_comms(lst, headers)
    results.extend(page_results)
        
    
    to_csv (results)
    

main()
