# Interface
import os.path
from splinter import Browser
from selenium import webdriver
import time

username="Cortex91Drahh"
password="password"

def login(username,password): #Cree un browser qui se connecte au site Showdown et se connecte au compte username password

    home = os.path.expanduser("~")
    path = {'executable_path': home + '/bin/chromedriver'} #Import avoir chromedriver dans ce dossier et l'avoir rendu executable

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") #Affiche la fenetre en grand
    options.add_argument("--disable-notifications") #Desactive les notifications chrome

    browser = Browser('chrome', **path, headless=False, options=options) #Crée le Browser

    browser.visit('https://play.pokemonshowdown.com/') #On se connecte au site showdown

    browser.find_by_tag('button[name="login"]').click() #Puis on manipule la page HTML avec des methodes scraping pour se connecter
    browser.find_by_tag('input[class="textbox autofocus"]').fill(username)
    browser.find_by_tag('button[type="submit"]').click()
    browser.find_by_tag('input[type="password"]').fill(password)
    browser.find_by_tag('button[type="submit"]').click()

    return browser #On return le browser pour continuer à l'utiliser


browser=login(username,password)
time.sleep(10)
browser.quit()