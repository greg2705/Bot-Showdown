# Interface
import os.path
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver

import time


def login(username,
          password):  # Cree un browser qui se connecte au site Showdown et se connecte au compte username password

    home = os.path.expanduser("~")
    path = {
        'executable_path': home + '/bin/chromedriver'}  # Import avoir chromedriver dans ce dossier et l'avoir rendu executable

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Affiche la fenetre en grand
    options.add_argument("--disable-notifications")  # Desactive les notifications chrome

    browser = Browser('chrome', **path, headless=False, options=options)  # Crée le Browser

    browser.visit('https://play.pokemonshowdown.com/')  # On se connecte au site showdown

    browser.find_by_tag(
        'button[name="login"]').click()  # Puis on manipule la page HTML avec des methodes scraping pour se connecter
    browser.find_by_tag('input[class="textbox autofocus"]').fill(username)
    browser.find_by_tag('button[type="submit"]').click()
    browser.find_by_tag('input[type="password"]').fill(password)
    browser.find_by_tag('button[type="submit"]').click()

    browser.find_by_tag('button[title="Sound"]').click()  # on mute l'horrible son du jeu
    browser.find_by_tag('input[name="muted"]').click()

    return browser  # On return le browser pour continuer à l'utiliser

def launch_game(browser,value):
    browser.find_by_tag('button[class="select formatselect"]').click()
    browser.find_by_tag('button[value="'+value+'"]').click()
    browser.find_by_tag('button[class="button mainmenu1 big"]').click()
    while(True):
        time.sleep(1)
        if(browser.is_element_present_by_tag('button[class="button timerbutton"]')):
            browser.find_by_tag('button[class="button timerbutton"]').click()
            browser.find_by_tag('button[name="timerOn"]').click()
            return browser


def move(browser, move):
    if move == "m1":
        browser.find_by_tag('textarea[class="textbox"]').last.fill("/move 1\n")
        return browser

    elif move == "m2":
        browser.find_by_tag('textarea[class="textbox"]').last.fill("/move 2\n")
        return browser

    elif move == "m3":
        browser.find_by_tag('textarea[class="textbox"]').last.fill("/move 3\n")
        return browser

    elif move == "m4":
        browser.find_by_tag('textarea[class="textbox"]').last.fill("/move 4\n")
        return browser

    elif move == "s2":
        browser.find_by_tag('textarea[class="textbox"]').last.fill("/switch 2\n")
        return browser

    elif move == "s3":
        browser.find_by_tag('textarea[class="textbox"]').last.fill("/switch 3\n")
        return browser

    elif move == "s4":
        browser.find_by_tag('textarea[class="textbox"]').last.fill("/switch 4\n")
        return browser

    elif move == "s5":
        browser.find_by_tag('textarea[class="textbox"]').last.fill("/switch 5\n")
        return browser

    elif move == "s6":
        browser.find_by_tag('textarea[class="textbox"]').last.fill("/switch 6\n")
        return browser

    return browser


def partie(browser):
    print("debut")
    endgame = False
    numberturn = 0
    while (endgame == False):
        html = BeautifulSoup(browser.html, 'html.parser')
        if (browser.is_element_present_by_tag('button[name="instantReplay"]')):
            endgame = True
        if(int(len(html.findAll("h2",class_='battle-history'))>numberturn)):
            numberturn+=1
            choix=str(input("Entrez votre attaque : "))
            move(browser,choix)
        time.sleep(2)
    print("Partie Finie")
    browser.quit()


browser = login("Cortex91Drahh", "password")
time.sleep(5)
launch_game(browser,"gen4randombattle")


