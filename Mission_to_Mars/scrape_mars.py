from splinter import Browswer
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless = False)

def scraping():
    browser = init_browser()
    mars_data = dict()
    
    url = 'https://mars.nasa.gov/news/?order=publish_date+desc&blank_scope=Latest'
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup