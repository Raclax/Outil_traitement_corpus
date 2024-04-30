from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Configuration du WebDriver
driver_path = '../geckodriver'  # Par exemple: '/usr/local/bin/geckodriver'
service = Service(executable_path=driver_path)
driver = webdriver.Firefox(service=service)

# Aller sur la page d'un produit Amazon
url = "https://www.amazon.fr/dp/B07PJV3JPR"  # Exemple d'URL d'un produit
driver.get(url)

# Attendre que les commentaires soient chargés et cliquer sur le lien 'Voir tous les commentaires'
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "acrCustomerReviewText"))
    )
    element.click()
except Exception as e:
    print(e)
    driver.quit()

# Extraction des commentaires et des notes
try:
    # Attendre que la page des commentaires soit chargée
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".review-text-content"))
    )
    # Boucle sur les commentaires
    comments = driver.find_elements(By.CSS_SELECTOR, ".review-text-content")
    ratings = driver.find_elements(By.CSS_SELECTOR, ".review-rating")

    for comment, rating in zip(comments, ratings):
        print("Note:", rating.text)
        print("Commentaire:", comment.text.strip())
except Exception as e:
    print(e)

# Fermeture du navigateur
driver.quit()
