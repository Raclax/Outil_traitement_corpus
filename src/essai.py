"""
Ce script permet de créer une liste de toutes les liens qui dirigent vers des pages d'articles amazon d'une certaine catégorie, ici books,
à partir du lien "de base", puis qu'en extraire les noms des clients qui ont laissés un commentaire, 
leur note et le texte du coimmentaire, pour le placer dans une liste de dictionnaires puis un CSV

"""

import requests
from bs4 import BeautifulSoup as soup
from time import sleep
import csv

def find_pages(url_base, headers):
    
    """
    Prends un url "de base" d'une page amazon et ressort une liste des urls des pages des produits de cette page.

    Parameters
    ----------
    url_base : str
        La première partie de l'url, qu'on va compléter avec les particularités de chaque url de pages
    headers : dict
        Le header qu'on va utiliser

    Returns
    -------
    lien : list
        une liste de strings qui correspond aux urls des pages des produits
    
    
    """

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

    """
    Prends une liste d'urls des pages d'un produit et ressort le pseudo, le commentaire et la note des personnes qui ont laissés une review.
    
    Parameters
    ----------
    lst : list
        La liste des urls des pages 
    headers : dict
        Le header qu'on va utiliser

    Returns
    -------
    tout : list
        Liste de dictionnaires contenant les pseudos, les commentaires et les notes en str et en int.
    """

    tout=[]
    for url in lst :
        html = requests.get(url, headers=headers)
        #print(response.status_code)  
        comms = soup(html.text, 'html.parser')
        #print(comms)
        comments = comms.find_all('span', {'class': 'a-size-base review-text review-text-content'})
        ratings = comms.find_all('span', {'class': 'a-icon-alt'})
        id = comms.find_all('span', {'class': 'a-profile-name'})

    for i in range (len(comments)):
        if len (ratings)
        tout.append({"Identifiant" : id[i].text.strip(),
                    "Commentaire" : comments[i].text.strip(),
                    "Note" : int(ratings[i].text.strop().split()[0]),
                    "Note_str" : ratings[i].text.strop().split()[0]
                    })
    return tout




def to_csv (tout) :

    """
    Prends la liste de dictionnaires et crée un fichier csv.

    Parameters
    ----------
    tout : list
        La liste des dictionnaires contenant les infos des reviews 
    
    """

    titres = ['Identifiant', 'Commentaire', 'Note', 'Note_str']

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
