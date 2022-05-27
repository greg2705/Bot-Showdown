# Interface
import os.path
import random

from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver

import time


def login(username,password):  # Cree un browser qui se connecte au site Showdown et se connecte au compte username password

    home = os.path.expanduser("~")
    path = {
        'executable_path': home + '/bin/chromedriver'}  # Import avoir chromedriver dans ce dossier et l'avoir rendu executable

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Affiche la fenetre en grand
    options.add_argument("--disable-notifications")  # Desactive les notifications chrome

    browser = Browser('chrome', **path, headless=False, options=options)  # Crée le Browser

    browser.visit('https://play.pokemonshowdown.com/')  # On se connecte au site showdown

    browser.find_by_tag('button[class=" css-1wrbm"]').click()

    browser.find_by_tag('button[name="login"]').click()  # Puis on manipule la page HTML avec des methodes scraping pour se connecter
    browser.find_by_tag('input[class="textbox autofocus"]').fill(username)
    browser.find_by_tag('button[type="submit"]').click()
    browser.find_by_tag('input[type="password"]').fill(password)
    browser.find_by_tag('button[type="submit"]').click()

    browser.find_by_tag('button[title="Sound"]').click()  # on mute l'horrible son du jeu
    browser.find_by_tag('input[name="muted"]').click()

    return browser  # On return le browser pour continuer à l'utiliser

def launch_game(browser,value): #Lance une game à partir d'un browser , value permet de choisir le mode de jeu
    browser.find_by_tag('button[class="select formatselect"]').click()
    browser.find_by_tag('button[value="'+value+'"]').click()
    browser.find_by_tag('button[class="button mainmenu1 big"]').click() #On choisit le mode de jeu et on lance la partie
    while(True): #Permet de detecter quand une partie est lancé
        time.sleep(1)
        if(browser.is_element_present_by_tag('button[class="button timerbutton"]')): #On lance le timer
            browser.find_by_tag('button[class="button timerbutton"]').click()
            browser.find_by_tag('button[name="timerOn"]').click()
            return browser


def partie(browser): #Permet le déroulement d'une partie
    endgame = False
    nbalive=6
    numberturn = 0 #On coute le nombre de tour pour savoir qaund il faut jouer
    while (endgame == False): #Boucle tant que la partie n'est pas fini
        html = BeautifulSoup(browser.html, 'html.parser')
        if (browser.is_element_present_by_tag('button[name="instantReplay"]')): #On regarde si la partie est finie
            endgame = True
        if(len(get_list_move(browser))>0):#Permet de savoir si on doit faire un move
            make_move(browser)
        time.sleep(1)

    browser.quit() #On quitte le jeu quand la partie est finie

def get_list_move(browser):
    if(browser.is_element_present_by_tag('button[name="chooseMove"]')):
        moov=browser.find_by_tag('button[name="chooseMove"]')
        moove=["m"+str(m.value) for m in moov]
    else:
        moove=[]
    if(browser.is_element_present_by_tag('button[name="chooseSwitch"]')):
        switc=browser.find_by_tag('button[name="chooseSwitch"]')
        switch=["s" + str(s.value) for s in switc]
    else:
        switch=[]
    return moove+switch

def make_move(browser):
    if(browser.is_element_present_by_tag('button[name="chooseMove"]')):
        moov=browser.find_by_tag('button[name="chooseMove"]')
        moove=["m"+str(m.value) for m in moov]
    else:
        moove=[]
    if(browser.is_element_present_by_tag('button[name="chooseSwitch"]')):
        switc=browser.find_by_tag('button[name="chooseSwitch"]')
        switch=["s" + str(s.value) for s in switc]
    else:
        switch=[]
    radn=random.choice(range(len(moove+switch)))
    if(radn<len(moove)):
        moov[radn].click()
    else:
        switc[radn-len(moove)].click()
    return

browser = login("Botshow","projetpython")
time.sleep(5)
launch_game(browser,"gen4randombattle")
partie(browser)

