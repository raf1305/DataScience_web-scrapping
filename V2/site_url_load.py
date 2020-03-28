from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#parsing the html page and return

def url_to_be_read(my_url):
    uClient = uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html5lib")
    return page_soup
