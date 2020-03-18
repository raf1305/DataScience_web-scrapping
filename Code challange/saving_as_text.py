#creating a text file with name as title and saving the article text

import re
def store_as_text(title,text):
    title=re.sub(r"\W", "_",title)
    text_create=title+".txt"
    f=open(text_create,"w")
    f.write(text)
    f.close()
    