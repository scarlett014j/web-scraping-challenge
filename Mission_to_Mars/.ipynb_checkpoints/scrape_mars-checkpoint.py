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
    
    #scraping title and description of most recent article
    title = soup.find('article').find('li', class_='slide').find('h3').text
    description = soup.find('article').find('li', class_='slide').find('div', class_='article_teaser_body').text
    mars_data["news_title"] = title
    mars_data["description"] = description
    
    #setting up url for picture scraping
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
realurl = 'https://www.jpl.nasa.gov'
browser.visit(url2)

    #visit second site
    html2 = browser.html
    soup2 = BeautifulSoup (html2, 'html.parser')
    
    #scraping image source
    image = soup2.find('footer').find('a', class_ ='button fancybox')
    image = realurl + image ['data-fancybox-href']
    mars_data["feature_image"] = image
    
    #pandas table scraping
    url3 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url3)
    df = tables[0]
    df.columns = ['Description', 'Mars']
    df.set_index('Description', inplace=True)
    html_table = df.to_html(classes = "data", index = False, header = True)
    mars_data["table"] = html_table

    #hemisphere name scraping
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    html4 = browser.html
    soup4 = BeautifulSoup(html4, 'html.parser')
    hemi = soup4.find_all('h3')
    hemispheres = [result.text[:-9] for result in hemi]
    mars_data["hemispheres"] = hemipspheres
    
    #different hemispheres images
    cerb_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(cerb_url)
    html_cerb = browser.html
    soup_cerb = BeautifulSoup(html_cerb, 'html.parser')
    cerberus = (soup_cerb.find_all('div', class_ = 'downloads')[0].li.a.get('href'))
    
    schiap_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(schiap_url)
    html_schiap = browser.html
    soup_schiap = BeautifulSoup(html_schiap, 'html.parser')
    schiaparelli = (soup_schiap.find_all('div', class_ = 'downloads' [0].li.a.get('href'))

    syrtis_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(syrtis_url)
    html_syrtis = browser.html
    soup_syrtis = BeautifulSoup(html_syrtis, 'html.parser')
    syrtis = (soup_syrtis.find_all('div', class_ = 'downloads')[0].li.a.get('href'))
      
    valles_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(valles_url)
    html_valles = browser.html
    soup_valles = BeautifulSoup(html_valles, 'html.parser')
    valles = (soup_valles.find_all('div', class_ = 'downloads')[0].li.a.get('href'))
    
    hemi_d = [
    {'title': 'Cerberus Hemisphere', 'img_url': cerberus},
    {'title': 'Schiaparelli Hemisphere', 'img_url': schiaparelli},
    {'title': 'Syrtis Major Hemisphere', 'img_url': syrtis},
    {'title': 'Valles Marineris Hemisphere', 'img_url': valles}
    ]
    
    mars_data["hemi_d"] = hemi_d
    return mars_data