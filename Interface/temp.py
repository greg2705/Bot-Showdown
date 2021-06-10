# Interface
import os.path
from splinter import Browser
from selenium import webdriver
import time



home = os.path.expanduser("~")

if(os.path.exists(home+'/bin/chromedriver')==False):
    hah=0

path = {'executable_path':home+'/bin/chromedriver'}

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

browser = Browser('chrome',**path,headless=False, options=options)

browser.visit('https://play.pokemonshowdown.com/')

time.sleep(10)
browser.quit()