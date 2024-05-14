"""Créateur de dataset

Ce script permet de récupérer toutes les pages articles à partir d'une page principale d'amazon pour ensuite en extraire les reviews : 
le texte, l'id de la personne et la note associée.

Ce script contient également one fonction pour transformer ces informations en un fichier CSV.

A noter que bien qu'il devrait fonctionner en théorie, en pratique ce n'est pas le cas :
Amazon fait en sorte que les données scrappées arrivent avec des soucis d'encodage et je n'ai pas tu y trouver de solution.

"""


import requests
from bs4 import BeautifulSoup as soup
from time import sleep
import csv

def find_pages(url_base, headers):
    
    """
    Parcourt les pages de liste de livres sur Amazon pour collecter les liens vers les pages individuelles des livres.

    Parameters
    ----------
    - url_base (str) : L'URL de base du site Amazon.
    - headers (dict) : le headers

    Returns
    -------
    - list : Une liste de strings contenant les URL des pages de détail des livres.

    En plus :
    - Pause de 2 secondes entre chaque requête pour éviter le blocage par le serveur d'Amazon.
    """
     
    page = 0
    lien = []
    while True:
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
        sleep(2) #2 secondes entre chque requêtes
    return lien

def find_comms (lst, headers):

    """
    Extrait les commentaires, les notes et les identifiants des utilisateurs à partir des pages de livres sur Amazon.
    
    Parameters
    ----------
    - lst (list) : Liste des URL des pages de livres à analyser.
    - headers (dict) : Les en-têtes HTTP utilisés pour les requêtes.

    Returns
    -------
    - list : Une liste de dictionnaires où chaque dictionnaire contient l'identifiant de l'utilisateur, le commentaire, 
             la note numérique et la note sous forme de texte.
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

        for i in range (0, len(comments)):
            if len (ratings) :
                tout.append({"Identifiant" : id[i].text.strip(),
                    "Commentaire" : comments[i].text.strip(),
                    "Note" : int(ratings[i].text.strop().split()[0]),
                    "Note_str" : ratings[i].text.strop().split()[0]
                    })
    return tout


def to_csv (tout) :
    
    """
    Sauvegarde les données extraites dans un fichier CSV.

    Parameters
    ----------
    - tout (list) : La liste des dictionnaires contenant les infos des reviews

    Returns
    -------
    - Crée un fichier 'dataset.csv' dans le répertoire de travail actuel et écrit les données dedans.
    """
    
    titres = ['Identifiant', 'Commentaire', 'Note', 'Note_str']

    with open('dataset.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=titres)
        writer.writeheader()

        for row in tout:
            writer.writerow(row)

def main():

    """
    Fonction principale.

    Parameters
    ----------
    - recherche (str) : Terme de recherche à utiliser pour filtrer les livres sur Amazon.
    - num_pages (int) : Nombre de pages à parcourir pour la collecte de liens.
    """

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
