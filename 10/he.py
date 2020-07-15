import re
import os
import requests
from bs4 import BeautifulSoup
import sklearn
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import urllib
import urllib3

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



import validators
from newspaper import Article



from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
import colorama

colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE

def outout(bow ,outputName,  o_path):
	f = open(o_path + "/" + outputName + ".txt" , 'w+', encoding='utf-8')
				
	f.write(str(bow))
			
	f.close

if __name__ == "__main__":
	site = input("Enter number to select category)")
	print(str(site))

	response = requests.get(site)
	soup = BeautifulSoup(response.text, 'html.parser')
	img_tags = soup.find_all('img')
	dirPath_F_score = "{}/{}".format("title", "title")
	os.makedirs(dirPath_F_score, exist_ok=True)
	urls = [img['src'] for img in img_tags]
	for url in urls:
		#print(url)
		filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
		if filename:
			with open(dirPath_F_score+filename.group(0), 'wb') as f:
				
				response = requests.get(url)
				f.write(response.content)