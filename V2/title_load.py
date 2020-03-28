from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
#extracting title from the article

def title_read(page_soup):
    header=page_soup.find("div",class_="story-body")    #this class contains the title information
    title=header.h1.get_text()
    title=re.sub(r"\W", "_",title)    
    return title