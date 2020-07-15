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



def main():

	array_topics = [
	'travel',
	'health',
	'national',
	'lifestyle'

	]


	def __choose_topics__(array_topics):
		

		for i in range(len(array_topics)):
			print(str(i + 1) + '. ' + str(array_topics[i]))

		
		print(str(len(array_topics)))
		doituong = 0
		check = 0
		while( (doituong <= 0) | (doituong >  len(array_topics) )  ):

			doituong = int(input("Enter number to select category, another to skip(enter to continute)"))
			check = doituong



		print(str(array_topics[check - 1]))















if __name__ == "__main__":
	main()



