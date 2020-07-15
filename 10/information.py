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


#import urllib.requesth

import json
import unicodedata
from unidecode import unidecode


#FROM LIB
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
def filterTexts(txtArr):
	res = []
	for i in range (len(txtArr)):   
                #loai bo html
		text_cleaned = clean_html(txtArr[i])
                    #tach cau
		sents = sent_tokenize(text_cleaned)
                    #Loai bo ky tu dac biet
		sents_cleaned = [remove_special_character(s) for s in sents]
                    #Noi cac cau lai thanh text
		text_sents1_join = ' '.join(sents_cleaned)
                    #tach tu
		words = word_tokenize(text_sents1_join)
                    #dua ve dag chu thhuong
		words = [word.lower() for word in words]
                    #loại bo hu tu
                #words = [word for word in words if word not in my_stopwords]
                    #Chuan hoa tu
		words = [ps.stem(word) for word in words]
                
		sample = ''
		for i in words:
			sample += i
			sample += " "

                
		res.append(sample)

	return res



def writeCountVectorizer(bow, bow1 ,outputName,  o_path):
	f = open(o_path + "/" + outputName + ".txt" , 'w+', encoding='utf-8')
            
	f.write(str(bow))
	f.write('\n')
	f.write(str(bow1))
	f.close

def writeTfidfVectorizer(bow, bow1, bow3 ,outputName,  o_path):
	f = open(o_path + "/" + outputName + ".txt" , 'w+', encoding='utf-8')
            
	f.write(str(bow))
	f.write('\n')
	f.write(str(bow1))
	f.write(str(bow1))

	f.close
	





def clean_html(text):
	soup = BeautifulSoup(text, 'html.parser')

	return soup.get_text()


def remove_special_character(text):
            #thay the ky tu dac biet bang ' '
	string = re.sub('[^\w\s]', ' ', text)
            #xu ly cac khoang trang thua o giua chuoi
	string = re.sub('\s+',' ', string)
            #xu li cac khoang trang thua dau va cuoi chuoi
	string = string.strip()
	return string
        #tach cau tach tu, loai bo hu tu, chuan hoa tu


def LuaChon():
	print("1. Phuong phap Bow")
	print("2. Phuong phap TF-IDf")
	doituong = int(input('Nhap phuong phap ban chon :'))

	return doituong



ps = PorterStemmer()



def browserFiles(path):
	list_path = []
	for root, dirs, files in os.walk(paht):
		for file in files:
			list_path.append(root + "/" + file)
	return list_path



def readFile(list_path):
	read_files = []
	i = 0
	for i in range(len(list_path)):
		read_file = open(list_path[i] , "r", encoding="utf8")
		a = read_file.readlines()
		a = ' '.join(a)
		read_files.append(a)
	return read_files



def __get_theme__(soup):
	array_theme = []
	infomation = soup.find_all('li', attrs={"class":"nav-bar__title-bar-links__secondary-link"})

	for section in infomation:
        
		if (section.find('a')):
			final = section.find('a')
			array_theme.append(final)
		else:
			array_theme.append(0)

	return array_theme


#url link  / page
def __get_url_theme__(soup):
	array_sample = []
	array_url_theme = []
	infomation = soup.find_all('li', attrs={"class":"nav-bar__title-bar-links__secondary-link"})

	for section in infomation: 
		if (section.find('a')):
			final = section.find('a')
			array_sample.append(final)
		else:
			array_sample.append(0)

	
	for data in array_sample:
		array_url_theme.append(str(data['href']))
		#print(data['href'])

	return array_url_theme




def __get_page__(soup):
	#<h3 class="vice-card-hed vice-card-hed--light vice-card__vice-card-hed"><a href="https://www.vice.com/en_us/article/pa75mg/joe-biden-thinks-weed-is-a-gateway-drug" class="vice-card-hed__link">Joe Biden Is Out Here Calling Weed a 'Gateway Drug' in 2019</a></h3>
	#<a href="https://www.vice.com/en_us/article/pa75mg/joe-biden-thinks-weed-is-a-gateway-drug" class="vice-card-hed__link">Joe Biden Is Out Here Calling Weed a 'Gateway Drug' in 2019</a>

	array_sample = []

	infomation = soup.find_all('h3', attrs={"class":"vice-card-hed vice-card-hed--light vice-card__vice-card-hed"})
	for section in infomation:
		if (section.find('a')):
			final = section.find('a', 'vice-card-hed__link')
			array_sample.append(final)
		else:
			array_sample.append(0)

	array_page = []
	for data in array_sample:
		array_page.append(str(data['href']))

	return array_page







def __theme__(array_theme):
	for i in range(len(array_theme)):
		print(str(i + 1 )+ '. ' + str(fix_encoding(array_theme[i].get_text())))




def __create_folder__(directory, array_theme, doituong):
	for i in range(len(array_theme)):
		if(doituong == i):
			directory = directory + '\\' + str(array_theme[i].get_text())
			try:
				if not os.path.exists(directory):
					os.makedirs(directory)
			except OSError:
				print ('Error: Creating directory. ' +  directory)





def EX():
	sel = Selector(response)
	sample = sel.xpath('//a[@class="topics-card__image-link"]').get(default='None') 
	#for res in response.css('ul.topics-all > li.topics-collection topics-page__topics-collection > ul.topics-collection__items > li.topics-collection__item > section.topics-card topics-collection__topics-card > a.topics-card__image-link'):
	for res in response.css('ul.topics-all > li > ul > section > a'):

	#quote': res.extract()
		yield {'final':sample }


#lay tong so page co trong chu de (example: 80)
def __tolal_pages__(url):
	
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	sample = []
	infomation = soup.find_all('span', attrs={"class":"paginator__progress--last-page p-t-1--xs"})
	
	for data in infomation:
		sample.append(data.get_text())
	

	return sample


#lay duoc 12 link moi page (example: 80page(1 page co 12link) = 80*12=960 link)

def __get_all_links__(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	array_sample = []
	infomation = soup.find_all('section', attrs={"class":"topics-card topics-collection__topics-card"})
#<section class="topics-card topics-collection__topics-card"><a class="topics-card__image-link" href="https://www.vice.com/en_asia/article/889q8p/is-it-okay-to-switch-off-when-news-gets-overwhelming"><div class="card-image topics-card__card-image"><div class="placeholder-image arp-1-1--sm arp-16-9--md arp-16-9--lg arp card-image__placeholder-image"><picture class="responsive-image responsive-image--loaded placeholder__image"><source media="(min-width: 1000px)" srcset="https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.3746xh;0xw,0.3187xh&amp;resize=534:* 1x, https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.3746xh;0xw,0.3187xh&amp;resize=1068:* 2x"><source media="(min-width: 700px)" srcset="https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.3746xh;0xw,0.3187xh&amp;resize=334:* 1x, https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.3746xh;0xw,0.3187xh&amp;resize=668:* 2x"><source media="(min-width: 0px)" srcset="https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.6667xh;0xw,0.258xh&amp;resize=160:* 1x, https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.6667xh;0xw,0.258xh&amp;resize=320:* 2x"><img class="responsive-image__img" alt=""></picture></div></div></a><div class="topics-card__content"><div class="topics-card__timestamp"><div class="ff--accent size--6 uppercased">3 days ago</div></div><div class=""><div class="topics-card__content-text"><a class="topics-card__heading-link" href="https://www.vice.com/en_asia/article/889q8p/is-it-okay-to-switch-off-when-news-gets-overwhelming"><h3 class="topics-card__heading ff--hed fw--bold lh--headline size--4 size--4-md size--3-lg size--3-xl">Is It Okay to Switch off When News Gets Overwhelming?</h3></a><p class="topics-card__dek ff--body fw--normal lh--body size--5">A handy guide for those finding it tough to cope with the horrible things happening in the world but also feeling guilty about looking away.</p><div class="byline topics-card__byline ff--accent fw--normal lh--headline size--6"><span class="byline__byline">Dhvani Solani </span></div></div></div></div></section>
#<a class="topics-card__image-link" href="https://www.vice.com/en_asia/article/889q8p/is-it-okay-to-switch-off-when-news-gets-overwhelming"><div class="card-image topics-card__card-image"><div class="placeholder-image arp-1-1--sm arp-16-9--md arp-16-9--lg arp card-image__placeholder-image"><picture class="responsive-image responsive-image--loaded placeholder__image"><source media="(min-width: 1000px)" srcset="https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.3746xh;0xw,0.3187xh&amp;resize=534:* 1x, https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.3746xh;0xw,0.3187xh&amp;resize=1068:* 2x"><source media="(min-width: 700px)" srcset="https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.3746xh;0xw,0.3187xh&amp;resize=334:* 1x, https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.3746xh;0xw,0.3187xh&amp;resize=668:* 2x"><source media="(min-width: 0px)" srcset="https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.6667xh;0xw,0.258xh&amp;resize=160:* 1x, https://video-images.vice.com/test-uploads/articles/5ee32fbbd340280095e0ea7d/lede/1591948242328-jonathan-borba-bLjPKYjulQ4-unsplash.jpeg?crop=1xw:0.6667xh;0xw,0.258xh&amp;resize=320:* 2x"><img class="responsive-image__img" alt=""></picture></div></div></a>
	for section in infomation:
		if (section.find('a')):
			final = section.find('a', 'topics-card__image-link')
			array_sample.append(final)
		else:
			array_sample.append(0)

	array_page = []
	for data in array_sample:
		array_page.append(str(data['href']))
	
	return array_page


def __get_name_all_links(url):
	#<h3 class="topics-card__heading ff--hed fw--bold lh--headline size--4 size--4-md size--3-lg size--3-xl">Is It Okay to Switch off When News Gets Overwhelming?</h3>
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	sample = []
	infomation = soup.find_all('h3', attrs={"class":"topics-card__heading ff--hed fw--bold lh--headline size--4 size--4-md size--3-lg size--3-xl"})
	
	for data in infomation:
		sample.append(data.get_text())
	

	return sample




#https://www.vice.com/en_asia/topic/lifestyle?page=2

	
def __get_final_pages__(url_crawl, site1):
	#https://www.vice.com/en_asia/topic/lifestyle?page=
	#url = url_crawl + '?page='
	#array_final2 = []
	#array_final2 = __get_all_links__(site1)
	total = []
	total = __tolal_pages__(str(site1))

	array_total = []

	urls = []
	for i in range(1,int(total[0]) + 1):
		url = (url_crawl + '?page=%s') % i
		urls.append(url)


	for y in range(len(urls)):
		array_final2 = []
		array_final2 = __get_all_links__(str(urls[y]))
		for data in array_final2:
			array_total.append(data)



	return array_total



def __get_get__(url):
	#<h3 class="topics-card__heading ff--hed fw--bold lh--headline size--4 size--4-md size--3-lg size--3-xl">Is It Okay to Switch off When News Gets Overwhelming?</h3>
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	sample = []
	infomation = soup.find_all('h3', attrs={"class":"topics-card__heading ff--hed fw--bold lh--headline size--4 size--4-md size--3-lg size--3-xl"})
	
	for data in infomation:
		sample.append(data.get_text())
	

	return sample







def main():
	#class="nav-bar__title-bar-links__primary-link"
	#https://www.vice.com/en_asia
	site = input('INPUT : ')
	corpus = [] 

	response = requests.get(site)
	soup = BeautifulSoup(response.text, 'html.parser')


	array_theme = __get_theme__(soup)

	__theme__(array_theme)

	doituong = int(input('Nhap phuong phap ban chon :'))


#lay chu de
	array_final = []
	array_final = __get_url_theme__(soup)


	for i in range(len(array_final)):
		print(str(array_final[i]))
	
	#https://www.vice.com/en_asia/topic/culture
	#https://www.vice.com/en_asia/topic/lifestyle
	#https://www.vice.com/en_asia/topic/lgbtq
	#https://www.vice.com/en_asia/topic/nsfw
	#https://www.vice.com/en_asia/topic/weird
	#https://www.vice.com/en_asia/topic/environmental-extremes
	#https://www.vice.com/en_asia/topic/video

#lay page trong chu de
	#https://www.vice.com/en_asia/topic/lifestyle?page=

	site1 = input('INPUT THEME PAGE : ')
	
	

#lay link page theo doi tuong
	url_crawl = array_final[doituong - 1]
	#print(str(url_crawl))


#lay total page
	

	total = []
	total = __tolal_pages__(str(site1))
	print(str(total[0]))


#link page
	array_final2 = []
	array_final2 = __get_all_links__(site1)

	#for i in range(len(array_final2)):
		#print(str(array_final2[i]))


#name link page
	array_final3 = []
	array_final3 = __get_name_all_links(site1)

	#for i in range(len(array_final3)):
		#print(str(array_final3[i]))



	array_final4 = []
	array_final4 = __get_final_pages__(url_crawl, site1)

	#for i in range(len(array_final4)):
		#print(str(array_final4[i]))










#https://www.vice.com/en_asia/topic/lifestyle?page=2

	#<div class="topics-card__content-text"><a class="topics-card__heading-link" href="https://www.vice.com/en_asia/article/bv8z3d/it-took-leaving-two-exes-with-drinking-problems-to-see-my-own"><h3 class="topics-card__heading ff--hed fw--bold lh--headline size--4 size--4-md size--3-lg size--3-xl">It Took Leaving Two Exes With Drinking Problems to See My Own</h3></a><p class="topics-card__dek ff--body fw--normal lh--body size--5">Loving and losing another drinker made me rethink my—and my community’s—relationship with alcohol.</p><div class="byline topics-card__byline ff--accent fw--normal lh--headline size--6"><span class="byline__byline">Lori Fox </span></div></div>
	
#<a class="topics-card__heading-link" href="https://www.vice.com/en_asia/article/bv8z3d/it-took-leaving-two-exes-with-drinking-problems-to-see-my-own"><h3 class="topics-card__heading ff--hed fw--bold lh--headline size--4 size--4-md size--3-lg size--3-xl">It Took Leaving Two Exes With Drinking Problems to See My Own</h3></a>

#<h3 class="topics-card__heading ff--hed fw--bold lh--headline size--4 size--4-md size--3-lg size--3-xl">It Took Leaving Two Exes With Drinking Problems to See My Own</h3>   


#_______total page___
#<span class="paginator__progress dsp-flex--xs flex-wrap grd-just-center-xs m-aut--xs ff--hed fw--bold size--4-sm size--3-md"><span class="paginator__progress--current-page p-b-1--xs">02</span><span class="paginator__progress--last-page p-t-1--xs">80</span></span>
#<span class="paginator__progress--current-page p-b-1--xs">02</span>
#<span class="paginator__progress--last-page p-t-1--xs">80</span>



	site22 = input('Nhap url(duong dan) trang web (https://tiki.vn/nha-sach-tiki/c8322?src=mega-menu&_lc=Vk4wMzkwMjAwMTU%3D&): ')
	
	corpus = []
	corpus  = __get_get__(site22)

	print(str(corpus))

	corpus_final = []
	corpus_final = filterTexts(corpus)
	print(str(corpus_final))
		
	check = LuaChon()

	if (check == 1):
		o_path = input('Nhap duong dan folder luu file( vd:  ): ')
		#outputName = input('Nhap ten file xuat ra: ')

		result = CountVectorizer()
		bow = result.fit_transform(corpus_final).todense()

		bow1 = result.vocabulary_

		writeCountVectorizer(bow , bow1, 'BoW', o_path)


	else:
		o_path = input('Nhap duong dan folder luu file( vd:  ): ')
		#outputName = input('Nhap ten file xuat ra: ')

		tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
		tf_idf_matrix = tf.fit_transform(corpus_final)
		feature_names = tf.get_feature_names()
		dense = tf_idf_matrix.todense()


		writeTfidfVectorizer(tf_idf_matrix, feature_names, dense, 'TF-IDF', o_path)

#C:\Users\DELL\Desktop

#https://www.vice.com/en_asia/article/y3mjav/quarantine-sucks-for-extroverts-but-its-not-fun-for-introverts-either-coronavirus-social-distancing





if __name__ == "__main__":
	main()

