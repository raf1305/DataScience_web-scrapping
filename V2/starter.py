from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sys
import site_url_load
import re
import title_load
import date_load
import text_load
import saving_as_text,data_store_in_csv,move_text_to_folder
import initiate_google_drive,text_file_upload,create_folder_google_drive
import os
import shutil
#extracting article text if the url contains any article
creds=None
folder_id=None
def site_test_for_article(page_soup):
    date=date_load.date_read(page_soup)
    title=title_load.title_read(page_soup)
    text=text_load.text_read(page_soup)
    saving_as_text.store_as_text(title,text)
    data_store_in_csv.data_write(title,date,my_url)
    text_file_upload.text_upload(title+'.txt',creds,folder_id)
    move_text_to_folder.move(title+'.txt')

#input from command line argument
search=sys.argv[1]
article_number=sys.argv[2]
article_num=int(article_number)

#parameter set search in title and article number
#search="coronavirus"
#article_num=20

#the news website we are searching
my_url="https://www.bbc.com/news"
page_soup=site_url_load.url_to_be_read(my_url)

#finding all the links in the page under anchor tag
texts=page_soup.find_all("a")

#a set to check duplicity of a url so we dont visit same url twice
links_passed=set()
#initiating google drive credentials
creds=initiate_google_drive.init_cred()
#creating a folder to store the texts in drive
folder_id=create_folder_google_drive.create_folder(creds)

#csv file to save links
f=open('final.csv','w')
f.write('Title'+','+'Date'+','+'Link'+'\n')
f.close()
#csv file to save google drive uploaded texts file id
f1=open('file_id.csv','w')
f1.write('Title'+','+'File_id'+'\n')
f1.close()

os.mkdir('Results')
for i in texts:
    #taking a url which has the string saved in variable "search" or the word "coronavirus"
    if(search in str(i).casefold() and "live" not in str(i).casefold()):  
        
        send=i.get('href')
        
        #some url does not have domain name but still reflect as link,adding domain name to visit webpage
        if("bbc.co" not in send):
            my_url="https://bbc.com"+str(send)

        #checking if the link is already visited or not  
        if(my_url not in links_passed):
            links_passed.add(my_url)
            
            try:
                page_soup=site_url_load.url_to_be_read(my_url)
                site_test_for_article(page_soup) #extracting article information if has any

                #counting number of article in the csv
                f = open("final.csv","r")
                num_lines = sum(1 for line in f)
                if(num_lines==article_num+1):
                    break
                f.close()

                #finding all the links and adding them in search for later queue "texts"
                temp=page_soup.find_all("a")
                texts.extend(temp)
            except:
                temp=page_soup.find_all("a")
                texts.extend(temp)
                pass
#uploading csv files to drive and moving to folder results
text_file_upload.text_upload('final.csv',creds,folder_id)
text_file_upload.text_upload('file_id.csv',creds,folder_id)

          
