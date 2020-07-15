import re
import os
import requests
from bs4 import BeautifulSoup
import sklearn
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
my_stopwords = set(stopwords.words('english') + list(punctuation))
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import urllib
#from urlparse import urlparse
from urllib.parse import urlparse
import scrapy

from ftfy import fix_encoding


import unicodedata
from unidecode import unidecode
def filt(word):
    return unicodedata.normalize('NFKD', word).encode('ascii', errors='ignore').decode('ascii')





def output(bow ,outputName,  o_path):
    f = open(o_path + "/" + outputName + ".txt" , 'w+', encoding='utf-8')
    f.write(str(bow))
    f.write('\n')
    f.close

def begin():
    #url website user input
    site_user_input = int(input('Nhap duong dan trang web(URL) can duyet :'))

    return site_user_input













def LuaChon():
    print("1. Giai tri")
    print("2. Phap luat")
    print("3. Doi song")
    print("4. Kinh te")
    print("5. Giao duc")
    print("6. The thao")
    print("7. Cong nghe")
    print("8. Oto xe may")
    doituong = int(input('Nhap chu de ban chon :'))

    return doituong




def main():

    #C:\Users\DELL\Desktop\output2.txt
    #https://tiki.vn/nha-sach-tiki/c8322?src=mega-menu&_lc=Vk4wMzkwMjAwMTU%3D&


    #https://eva.vn

    #https://www.tinmoi.vn




    site = input('Nhap url(duong dan) trang web: ')
    folder_path = "Giai_tri1"
    check = LuaChon()
    





    if (check == 1):
        print("1. Giai tri")
        folder_path = "Giai_tri"
        newpath = r'C:\Users\DELL\Desktop\Giai_tri' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)


    elif(check == 2):
        print("2. Phap luat")
    elif(check == 3):
        print("3. Doi song")
    elif(check == 4):
        print("4. Kinh te")
    elif(check == 5):
        print("5. Giao duc")
    elif(check == 6):
        print("6. The thao")
    elif(check == 7):
        print("7. Cong nghe")
    else:
        print("8. Oto xe may")
















    corpus = []
    

    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    #product_names = soup.find_all('a' )


    #h3 = soup.find_all('img', attrs={"class":"embed-responsive-item lazyload-img"})
   # for h in h3:
      #  print(str(h['alt']))


    


#0606

    array_h2 = []
    array_h3 = []
#div class="post-tags"
    infomation = soup.find_all('div', attrs={"class":"media-body"})

    for section in infomation:
        
        if (section.find('h2', 'h3 mt-0 my-2')):
            final = section.find('h2', 'h3 mt-0 my-2')
            array_h2.append(final)
        else:
            array_h2.append(0)

        #if (section.find('h3', 'mt-0 my-2')):
          # final1 = section.find('h3', 'mt-0 my-2')
           # array_h3.append(final1)
        #else:
           # array_h3.append(0)



    infomation1 = soup.find_all('div', attrs={"class":"post-tags"})
    for section1 in infomation1:
            if(section1.find('h3', 'mt-0 my-2')):
                final = section1.find('h3', 'mt-0 my-2')
                array_h3.append(final)
            else:
                array_h3.append(final)




    infomation2 = soup.find_all('h3', attrs={"class":"mt-0 my-2"})

    for i in range(len(infomation2)):
        #print(product_names[i].get_text().decode('ISO-8859-1'))
        #print(str(filt(product_names[i].get_text())))
       # print(unidecode(product_names[i].get_text()))
        #print(str(product_names[i].get_text().encode('ascii','utf-8')))
        #print(product_names[i].get_text().decode('utf8').encode('latin1').decode('utf8'))
        print(str(fix_encoding(infomation2[i].get_text())))

    



    
    #print(str(array_h2))
    #print(str(array_h3))
    
    for i in range(len(array_h2)):
        print(str(fix_encoding(array_h2[i].get_text())))

    




















#Sức khỏe
    #all_links = soup.find_all('a', attrs={"class":"actv clrFeatr bld"})

    #for all_link in all_links:
        #print(str(all_link['title']))





    #links_tinmoi = soup.find_all('a', attrs={"class":"nav-link"})

    #for link_tinmoi in links_tinmoi:
        #print(str(link_tinmoi['href']))






    #books = soup.find('a').text
##    links = soup.find_all('a', attrs={"class":"lgoEva"})
    #page_content.find('p', attrs={"class":"title"})
    #for book in books:
        #print(str(book))

    #o = urlparse (site)
##    for link in links:
##      print(urlparse(link['href']).geturl())

    #o.geturl()

    #metatags = soup.find_all('meta',attrs={'name':'generator'})



    #Lay KeyWord Website

##    corpus = []

##    o_path = r'C:\Users\DELL\Desktop'
    #metatags = soup.find_all('meta', attrs={'name':'keywords'})
   #for tag in metatags:

       # print(str(tag['content']))
      # #output(tag['content'], 'keywords-web', o_path)


















if __name__ == "__main__":
    main()