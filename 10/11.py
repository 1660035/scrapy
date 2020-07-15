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

from urllib.parse import urlparse
import scrapy

from ftfy import fix_encoding


import urllib.request

import json
import unicodedata
from unidecode import unidecode    
#scrapy startproject f319 
#scrapy crawl threads


from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

from urllib import parse as UrlParser
from pyquery import PyQuery
import newspaper

import validators
from newspaper import Article


from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
internal_urls = set()
external_urls = set()

total_urls_visited = 0

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def crawl(url, max_urls=50):
   
	global total_urls_visited
	total_urls_visited += 1
	links = get_all_website_links(url)
	for link in links:
		if total_urls_visited > max_urls:
			break
		crawl(link, max_urls=max_urls)



def get_all_website_links(url):
	urls = set()
    # domain name of the URL without the protocol
	domain_name = urlparse(url).netloc
    # initialize an HTTP session
	session = HTMLSession()
    # make HTTP request & retrieve response
	response = session.get(url)
    # execute Javascript
	try:
		response.html.render()
	except:
		pass
	soup = BeautifulSoup(response.html.html, "html.parser")
	for a_tag in soup.findAll("a"):
		href = a_tag.attrs.get("href")
		if href == "" or href is None:
            # href empty tag
			continue
        # join the URL if it's relative (not absolute link)
		href = urljoin(url, href)
		parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
		href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
		if not is_valid(href):
            # not a valid URL
			continue
		if href in internal_urls:
            # already in the set
			continue
		if domain_name not in href:
            # external link
			if href not in external_urls:
                #print(f"[!] External link: {href}")
				external_urls.add(href)
			continue
		print(f"[*] Internal link: {href}")
		urls.add(href)
		internal_urls.add(href)

	#urls = internal_urls
	return urls












def Xuly(site):
#site = 'https://tiki.vn/nha-sach-tiki/c8322?src=mega-menu&_lc=Vk4wMzkwMjAwMTU%3D&'

	response = requests.get(site)
	soup = BeautifulSoup(response.text, 'html.parser')
	product_names = soup.find_all('div')

	type(product_names)
	titles = []
	for i in range(len(product_names)):
		if product_names[i].has_attr('data-title'): 
	 		titles.append(product_names[i]['data-title'])

	#for i in range(len(titles)):
		#print(str(titles[i]))

	return titles[0:5]


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

def get_text(file):
    read_file = open(file, "r", encoding="utf8")
    text = read_file.readlines()
    text = ' '.join(text)
    return text

def clean_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()


ps = PorterStemmer()

def main():

	#C:\Users\DELL\Desktop
	#https://tiki.vn/nha-sach-tiki/c8322?src=mega-menu&_lc=Vk4wMzkwMjAwMTU%3D&

	site = input('Nhap url(duong dan) trang web (https://tiki.vn/nha-sach-tiki/c8322?src=mega-menu&_lc=Vk4wMzkwMjAwMTU%3D&): ')
	
	corpus = []
	corpus  = Xuly(site)


	print(str(corpus))

	for data in corpus:
		print(str(data))

	
	sitsite = "https://www.news.com.au/"
	sample1 = []
	#sample1 = get_all_website_links(sitsite)

	
	import argparse
	parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
	
	    
	args = parser.parse_args()
	url = args.url
	max_urls = args.max_urls


	crawl(sitsite, max_urls=50)


	print("[+] Total Internal links:", len(internal_urls))
	print("[+] Total External links:", len(external_urls))
	print("[+] Total URLs:", len(external_urls) + len(internal_urls))


	#print(str(corpus))

	

	#for data in internal_urls():
		#print(str(data))

	#for data in external_urls():
		#print(str(data))




	corpus_final = []
	corpus_final = filterTexts(corpus)

	

	response1 = requests.get('https://www.news.com.au/sport/cycling')
	soup1 = BeautifulSoup(response1.text, 'html.parser')

	sample = []
	infomation = soup1.find_all('a')
            
	for data in infomation:
		sample.append(data['href'])
            
	for data1 in sample:
		print(str(data1))  



		
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

	
		#f_out = open(o_path + "\\" + outputName, 'a',encoding='utf-8')






	#f_out.write(str(bow))
	#f_out.write('\n')
	#f_out.write(str(bow1))
	#f_out.write(str(corpus_final))


if __name__ == "__main__":
	main()
