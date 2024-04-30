#from time import slip 
import requests
from bs4 import BeautifulSoup as soup
import csv

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0.',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }

#proxies = {"http":"159.65.245.255", "https" : "159.65.245.255"}
tout = []
url = 'https://www.amazon.com/Amazon-Essentials-Flat-Front-Shorts-3-Pack/dp/B08N7LDF1C?ref_=Oct_DLandingS_D_cfbdca2f_19&th=1'
html = requests.get(url, headers=headers)
comms = soup(html.text, 'html.parser')
#print (comms)

comments = comms.find_all('span', {'class': 'a-size-base review-text review-text-content'})
ratings = comms.find_all('span', {'class': 'a-icon-alt'})
id = comms.find_all('span', {'class': 'a-profile-name'})

for i in range (0, len(comments)):
    tout.append({"Identifiant" : id[i],
                "Commentaire" : comments[i],
                "Note" : int(ratings[i]),
                "Note_str" : ratings[i]
                })
    
titres = ['id', 'text', 'label', 'label_text']

with open('dataset.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=titres)
    writer.writeheader()

    for row in tout:
        writer.writerow(row)

