from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#loading the article text and return the whole article text as string

def text_read(page_soup):
    inner=page_soup.find("div",class_="story-body__inner")  #all the "p" tags under this class contain article text
    texts=inner.find_all("p")
    text=str()
    for i in texts:
        text=text+i.text+"\n"
    return text