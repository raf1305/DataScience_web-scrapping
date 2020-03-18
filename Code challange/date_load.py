from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#extracting date from the article

def date_read(page_soup):
    dates=page_soup.find("div",class_="mini-info-list-wrap") #this class contains date information
    date=dates.ul.li.div.text
    return date