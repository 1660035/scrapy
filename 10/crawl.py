#IMPORT LIB

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

#FROM LIB
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from bs4 import BeautifulSoup

#=============URL===================#
# https://vov.vn
# 


#CLASS
class ThreadsSpider(scrapy.Spider):
	
	name = "Sample-Index"
	start_urls = ['https://www.mercurynews.com/news/']
	custom_settings = {}
	
	#===============================#
	def parse(self, response):
		title =  response.xpath('//title/text()').get()
		sel = Selector(response)
		sample = sel.xpath('//a[@data-list-type="Header"]/text').get()
		array_theme = []
		

		final = sel.xpath('//a[contains(@href, "https://www.mercurynews.com/")]/@href').getall()
		final1 = sel.css('a[href*=https://www.mercurynews.com/]::attr(href)').getall()


		for res in response.css('ul.menu > li > ul.sub-menu > li > a'):
			#quote': res.extract()
			yield {'final': final, 'final1': final1 }







#DEF
def ExtractLine(object):
	#def process_item(self, item, spider):


	def __remove_html_tags__(self, text):
		html_tags = re.compile('<.*?>')
		return re.sub(html_tags, '', text)

	def __string_standardize__(self, text):
		text = text.strip("\n")
		text = text.strip()
		return text

	def __clean_html__(self, text):
		soup = BeautifulSoup(text, 'html.parser')
		return soup.get_text()

	def __remove_speacial_character__(self, text):
		string = re.sub('[^\w\s]', ' ', text)
		string = re.sub('\s+',' ', string)
		string = string.strip()
		return string

	def __filterTexts(self, text):
		res = []
		for i in range(len(text)):
			text_cleaned = __clean_html__(text[i])
			sents =  sent_tokenize(text_cleaned)
			sents_cleaned = [__remove_speacial_character__(s) for s in sents]
			text_sents_join = ' '.join(sents_cleaned)
			words = word_tokenize(text_sents_join)
			words = [words.lower() for word in words]
			words = [ps.stem(word) for word in words]
			sample_text = ''
			for i in words:
				sample_text += i
				sample_text += " "	
			res.append(sample_text)
		return res



	def __parse__(self, response):
		for i in range()




#<span class="paginator__progress dsp-flex--xs flex-wrap grd-just-center-xs m-aut--xs ff--hed fw--bold size--4-sm size--3-md"><span class="paginator__progress--current-page p-b-1--xs">02</span><span class="paginator__progress--last-page p-t-1--xs">80</span></span>
#<span class="paginator__progress--current-page p-b-1--xs">02</span>
#<span class="paginator__progress--last-page p-t-1--xs">80</span>


def filt(word):
            return unicodedata.normalize('NFKD', word).encode('ascii', errors='ignore').decode('ascii')


        def output(bow ,outputName,  o_path):
            f = open(o_path + "/" + outputName + ".txt" , 'w+', encoding='utf-8')
            f.write(str(bow))
            f.write('\n')
            f.close

        def begin():
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
            


        


        def getUrlTheme(directory, doituong):
            urlTheme = ''
            sampleUrl = ['chinh-tri', 'doi-song', 'the-gioi', 'kinh-te', 'xa-hoi',
            'phap-luat', 'the-thao', 'van-hoa-giai-tri', 'quan-su-quoc-phong',
             'suc-khoe', 'e-magazine', 'oto-xe-may']
            
            doituong = int(doituong - 1)
            urlTheme = directory + '\\' + str(sampleUrl[doituong])


            return urlTheme


        def createFolder(directory, array_theme, doituong):
            folder_path = ""
            for i in range(len(array_theme)):
                if(doituong == i):
                    directory = directory + '\\' + str(array_theme[i].get_text())

                    try:
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                    except OSError:
                        print ('Error: Creating directory. ' +  directory)


        def LuaChon(array_theme, doituong, o_path):
            for i in range(len(array_theme)):
                if(doituong == i):
                    themeFolder(o_path, str(array_theme[i].get_text()))


        i = 1  
        
        while True: 
            site = input('Nhap url(duong dan) trang web: ')
            r = requests.get(site)
            check =  r.status_code

            if(check == 200):  
                break 



        response = requests.get(site)
        soup = BeautifulSoup(response.text, 'html.parser')
       


        array_theme = []
        infomation = soup.find_all('li', attrs={"class":"nav__parent"})
        for section in infomation:
            
            if (section.find('a')):
                final = section.find('a')
                array_theme.append(final)
            else:
                array_theme.append(0)



        theme(array_theme)
        o_path = input('Nhap duong dan folder luu file: ')
        doituong = int(input('Nhap phuong phap ban chon :'))

        
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









