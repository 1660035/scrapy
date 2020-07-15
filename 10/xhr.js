let xhr = new XMLHttpRequest();-
xhr.open('get', 'https://jsonplaceholder.typicode.com/posts/1');
xhr.send();

xhr.onload = function() {
    console.log(xhr.response);
};


import scrapy
import os
#scrapy startproject f319 
#scrapy crawl threads
class ThreadsSpider(scrapy.Spider):
    name = "threads"
    folder_path = "save_file10"
    def start_requests(self):
        os.mkdir(self.folder_path)
        urls = []
        for i in range(2,500):
            #http://www.bongda.com.vn/champions-league/p2
            #url = 'https://eva.vn/lang-sao-c20.html?page=%s'% i
            #url = 'https://www.tinmoi.vn/phap-luat/page/%s' % i
            url = 'https://vov.vn/phap-luat/trang%s' % i
            #url = 'http://f319.com/forums/thi-truong-chung-khoan.3/page-%s'% i
            urls.append(url)
            
        for url in urls:        
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #page = response.url.split("-")
        page = response.url.split("/trang")
        #page = response.url.split("/")
        #page = response.url
        if len(page) < 2: 
            page = 1
        else:
            page = page[-1]
        filename = 'page-%s.html' % page
        


        
        
        with open(self.folder_path+"/"+filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file3 %s' % filename)

    





##########################3333
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


import urllib.request

import json
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



def theme(array_theme):
    id_theme = []
    for i in range(len(array_theme)):
        id_theme.append(i)
        print(str(i)+ '. ' + str(fix_encoding(array_theme[i].get_text())))




def themeFolder(o_path, themeNamee):

    f = open(o_path + "/" + themeNamee, 'wb')
    f.close
    


def LuaChon(array_theme, doituong, o_path):

    for i in range(len(array_theme)):
        if(doituong == i):
            themeFolder(o_path, str(array_theme[i].get_text()))



def createFolder(directory, array_theme, doituong):
    for i in range(len(array_theme)):
        if(doituong == i):
            directory = directory + '\\' + str(array_theme[i].get_text())
            try:
                if not os.path.exists(directory):
                    os.makedirs(directory)
            except OSError:
                print ('Error: Creating directory. ' +  directory)

        


def main():

    #C:\Users\DELL\Desktop\output2.txt
    #https://tiki.vn/nha-sach-tiki/c8322?src=mega-menu&_lc=Vk4wMzkwMjAwMTU%3D&


    #https://eva.vn

    #https://www.tinmoi.vn


#span class="desc


    #r = requests.get('https://vov.vn/van-hoa/nghe-si/hong-diem-dong-it-phim-la-loi-the-cua-toi-1055891.vov')
   # print(r.headers)


    

    



    i = 1  
    
    while True: 
        site = input('Nhap url(duong dan) trang web: ')
        r = requests.get(site)
        check =  r.status_code

        if(check == 200):  
            break 








    

    corpus = []
    

    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
   

#Lay chu de cua trang web
    array_theme = []
    infomation = soup.find_all('li', attrs={"class":"nav__parent"})

    


    for section in infomation:
        
        if (section.find('a')):
            final = section.find('a')
            array_theme.append(final)
        else:
            array_theme.append(0)


    for i in range(len(array_theme)):
        print(str(fix_encoding(array_theme[i].get_text())))






    theme(array_theme)
    o_path = input('Nhap duong dan folder luu file: ')
    doituong = int(input('Nhap phuong phap ban chon :'))

    #LuaChon(array_theme, doituong, o_path)

    createFolder(o_path, array_theme, doituong)
    



    htmlText = urllib.request.urlopen("https://vov.vn/api/comments.json?v=1591595725167&action=get&id=711714&page=1")

    data = json.load(htmlText)



    print (data["comments"])


    array = []
    array = data["comments"]
    print(str(array[0]['Comment']))










    links_tinmoi = soup.find_all('a', attrs={"class":"cms-link"})

    for link_tinmoi in links_tinmoi:
        print(str(link_tinmoi['href']))



























#scrapy startproject f319 
#scrapy crawl threads












if __name__ == "__main__":
    main()




##
Yêu cầu đối với chương trình:
1. Thu thập dữ liệu:
 Sử dụng crawler thu thập dữ liệu từ Internet theo chủ đề (yêu cầu
ít nhất 10 chủ đề, mỗi chủ đề ít nhất 50 văn bản).
 Đánh chỉ mục cho toàn bộ văn bản và chủ đề tương ứng của văn
bản để phục vụ quá trình phân loại và đánh giá ở các bước sau.
 Chia dữ liệu thành 2 tập con: Tập huấn luyện (train) và tập kiểm
thử (test).

2. Tiền xử lý dữ liệu: làm sạch, loại bỏ stopword, tách từ....
3. Biểu diễn văn bản sử dụng phương pháp TF-IDF.