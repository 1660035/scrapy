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

class ThreadsSpider(scrapy.Spider):
	name = "vy"
    #folder_path = "lo-gi"
	url = input("Input website's url: ")
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	def start_requests(self):
  		#Kiem tra URL hop le
		def __is_url__(url):
			return validators.url(url)

		def __get_theme__(url):
			cnn_paper = newspaper.build(url)
			topics = []
			for category in cnn_paper.category_urls():
				category.split(r'https://www.news.com.au/world')
				topics.append(category)
			return topics



		
		    	#https://www.news.com.au/world
		corpus = [] 
		corpus = __get_theme__(self.url)
		for data in corpus:
			print(str(data))



	