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

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()


from urllib.parse import unquote
from pathlib import PurePosixPath
import random2

total_urls_visited = 0





class ThreadsSpider(scrapy.Spider):
	name = "vy"
    #folder_path = "lo-gi"
	print("================================SCRAPY-WEBSITE================================")
	url = input("Input website's url: ")
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	parsedUrl = UrlParser.urlparse(url)

	my_stopwords = set(stopwords.words('english') + list(punctuation))

	supportCategories = [
	'national', 
	'world', 
	'lifestyle',
	'travel', 
	'entertainment',
	'technology', 
	'finance',
	'sport',
	'news',
	'sports',
	'entertainments'
	]

	supportCategories = [re.sub(r"\s|-", '', category) for category in supportCategories]

	def parse(self, response):
		

		
		#sef = crawl(response.url)

		article = Article(response.url)
		article.download()
		article.parse()

		sef = {'title':article.title}


		fol =response.meta.get('folder_pat')

		filename = '%s.txt' % (sef['title'] + str(random2.randint(1,1000)))


		with open(fol+"/"+filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file3 %s' % filename)



	def start_requests(self):
  		#Kiem tra URL hop le
		def __is_url__(self):
			return validators.url(url)

		def crawl(url):
			
			article = Article(url)
			article.download()
			article.parser()

			result = {'title':article.title}

			return result




		def writeText(path, content):
			file = open(path, "w", encoding="utf-8")
			if isinstance(content, str):
				file.write(content)
			elif (isinstance(content, collections.abc.Iterable)):
				for item in content:
					file.write(item + '\n')

			file.close()
		


		def __get_all_link_backup(url):
			response = requests.get(url)
			soup = BeautifulSoup(response.text, 'html.parser')
			all_link = []
			information = soup.find_all('a')

			for data in information:
				all_link.append(data['href'])

			return all_link



		def __get_categories__(url,response, supportCategories):
			if (response.status_code != 200):
				return None, 'status code is not 200'

			parsedUrl = UrlParser.urlparse(url)

			doc = PyQuery(response.text)
			all_links = doc('a[href]')

			processedlink = {}
			categories = []
			for link in all_links:
				link = doc(link)
				href = link.attr('href')
				parsedhref = UrlParser.urlparse(href)
				if not bool(parsedhref.hostname):
					href = "{}://{}{}".format(parsedUrl.scheme, parsedUrl.hostname, href)

				if href in processedlink:
					continue

				processedlink[href] = True

				title = link.text().strip()
				title_ = title.lower()
				title_ = re.sub(r"\s|-", '', title_)

				if title_ in supportCategories:
					categories.append((href, title))

			return categories, None				

		def __get_text__(file):
			read_file = open(file, "r", encoding="utf-8")
			text = read_file.readlines()
			text = ' '.join(text)
			return text

		def __clean_html__(text):
			soup = BeautifulSoup(text, "html.parser")
			return soup.get_text()

		def __remove_special_character(text):
			string = re.sub('[^\w\s]', '', text)
			string = re.sub('\s+', ' ', string)
			string = string.strip()
			return string

		def __filter_texts__(txtArr):
			res = []
			for i in range(len(txtArr)):
				text_cleaned = __clean_html__(txtArr[i])
				sents = sent_tokenize(text_cleaned)
				sents_cleaned = [__remove_special_character(s) for s in sents]
				text_sents_join = ' '.join(sents_cleaned)
				words = word_tokenize(text_sents_join)
				words = [word.lower() for word in words]
				words = [ps.stem(word) for word in words]

				sample = ''
				for i in words:
					sample += i 
					sample += " "

				res.append(sample)

			return res

		def writeText(path, content):
			file = open(path, "w", encoding="utf-8")
			if isinstance(content, str):
				file.write(content)
			elif (isinstance(content, collections.abc.Iterable)):
				for item in content:
					file.write(item + '\n')

			file.close()

		def writeCountVectorizer(bow, bow1 ,outputName,  o_path):
			f = open(o_path + "/" + outputName + ".txt" , 'w+', encoding='utf-8')
				
			f.write(str(bow))
			f.write('\n')
			f.write(str(bow1))
			f.close

		def outout(bow ,outputName,  o_path):
			f = open(o_path + "/" + outputName + ".txt" , 'w+', encoding='utf-8')
				
			f.write(str(bow))
			
			f.close


		def writeTfidfVectorizer(bow, bow1, bow3 ,outputName,  o_path):
			f = open(o_path + "/" + outputName + ".txt" , 'w+', encoding='utf-8')
			
			f.write(str(bow))
			f.write('\n')
			f.write(str(bow1))
			f.write(str(bow1))

			f.close

		def CosiSim(x):
			cosinearry = []
			myarray = []
			j = z = 0
			v = 1.00
			while z < len(x):
				while j < len(x):
					v = float(cosine_similarity(x[z],x[j]))
					myarray.append(round(v,2))
					j += 1
				cosinearry.append(myarray)
				z += 1
			return cosinearry





			def __topics__(array_topics):
				for i in range(len(array_topics)):
					print(str(i + 1) + '. ' + str(array_topics))


			def __choose_topics__(array_topics):
				for i in range(len(array_topics)):
					print(str(i + 1) + '. ' + str(array_topics))

				
		


		def __BoW__(array):
			result = CountVectorizer()
			bow = result.fit_transform(array).todense()
			bow1 = result.vocabulary_

			array_BoW = []
			array_BoW.append((bow, bow1))

			return array_BoW


		def __TF_IDF__(array):
			tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
			tf_idf_matrix = tf.fit_transform(corpus_final)
			feature_names = tf.get_feature_names()
			dense = tf_idf_matrix.todense()

			array_TF_IDF = []
			array_TF_IDF.append((tf_idf_matrix, feature_names, dense))

			return array_TF_IDF


		def __show_topics__(categories):
			print("========================CATEGORY=========================")

			for i in range(len(categories)):
				print('   ' + str(i + 1) + '. ' + str(categories[i][1]))
			print("=========================================================")


		def __hylt__(array_list, categories):
			array_result = []

			for data in array_list:
				#print(str(data[1]))
				if (categories[-1] == "/"):

					url = categories  
				else:
					url = categories  + "/"

				for x in range(len(data)):
					if (x != 0):
						temp = []
						for y in data[x]:
							temp.append(y)
						#print(str(temp[0]))
			
							url = url + str(temp[0]) + "/"
						#print(str(url))
						array_result.append(str(url))

				#print(str(url))
				#print("\n")


			return array_result

		def __url_hylt__(array_list, categories):
			array_result = []
			
			for data in array_list:
				response1 = requests.get(data)
				soup1 = BeautifulSoup(response1.text, 'html.parser')
				
				infomation = soup1.find_all('uri')
				print(str(len(infomation)))


				check = "https://edition.cnn.com/entertainment/"
				count_ = 1



	            
				for x in infomation:
					array_result.append(x)
					print(str(x))
					








			return array_result

		def __show_hylt__(array):
			chee = []
			for data in array:
				chee.append(str(data[1]))


			list_set = set(chee) 
		    # convert the set to the list 
			unique_list = (list(list_set)) 
			for data in unique_list: 
				print(f"{YELLOW}[*] :  {data}{RESET}")




		def unique(list1): 
	      
		    # insert the list to the set 
			list_set = set(list1) 
		    # convert the set to the list 
			unique_list = (list(list_set)) 
			array = []	
			for data in unique_list: 
				print(f"{YELLOW}[*] Internal link: {data}{RESET}")
				array.append(data)
			return array



		def is_valid(url):
		    """
		    Checks whether `url` is a valid URL.
		    """
		    parsed = urlparse(url)
		    return bool(parsed.netloc) and bool(parsed.scheme)
		def myFunc(e):
		    return len(e)
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
		def __show_elements_topics__(categories):
			url = categories
			print(str(url))
			urls = set()
	    # domain name of the URL without the protocol
	#22-06
			domain_name = urlparse(url).netloc
		    #domain_name_backup = "https://www.news.com.au/travel/"
		    
		    #print(str(domain_name))
		    #domain_name = urlparse(url).netloc
		    # initialize an HTTP session
			session = HTMLSession()
		    # make HTTP request & retrieve response
			response = session.get(url)



			sample_de =PurePosixPath(
		            unquote (
		                    urlparse(
		                            url
		                        ).path
		                )
		            ).parts[1]

			#print(str(sample_de))




		    # execute Javascript
			try:
				response.html.render()
			except:
				pass
			soup = BeautifulSoup(response.html.html, "html.parser")
			array_root = [] #/
			array_root_1 = []   #travel
			array_root_2 = []   #(travel,destinations)
			array_root_3 = []   #(destinations, europe)
			array_root_4 = []   #(europe, etc....)


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

		        #print(str(href))

		    


				count_sample = PurePosixPath(
		            unquote (
		                    urlparse(
		                            href
		                        ).path
		                )
		            ).parts

				count_count = len(count_sample)

		#get ROOT_1
				i = 0
				for i in range(len(count_sample)):
					sample = PurePosixPath(
					unquote (
		                    urlparse(
		                            href
		                        ).path
		                )
		            ).parts[i]
					domain_name_sample = urlparse(href).netloc
					if(i == 1):
						sample1 = PurePosixPath(
					unquote (
		                    urlparse(
		                            href
		                        ).path
		                )
		            ).parts[1]
						if((sample_de == sample1) &(domain_name == domain_name_sample) ):
							array_root_1.append(href)
							break


					if((sample_de == sample) & (domain_name == domain_name_sample)):
						array_root.append(href)
						break



		
			max_count_root = 0
			for data in array_root_1:

				count_root = PurePosixPath(
		                unquote (
		                        urlparse(
		                                data
		                            ).path
		                    )
		                ).parts

				count_count = len(count_root)
				if(count_count > max_count_root):
					max_count_root = count_count   




			#print(str(max_count_root))
			check = 2 

			array_root_de = [set() for i in range(max_count_root - 3)]
		#lotsosets[0].add('see me?')
			
			temp = []
			#print(array_root_de)

			for data_root1 in array_root_1:
				count_data_root1 = len(PurePosixPath(unquote(urlparse(data_root1).path)).parts)
		        
				if( count_data_root1 >= 3 ):
					#print('--------------------------------------------------------------')

					#print(f"{BLUE} {data_root1}{RESET}")
					#print(f"{GREEN}: {count_data_root1}{RESET}")
					index = [set() for i in range(count_data_root1 - 1 )]
					#print(index)

					for i in range (1, count_data_root1 ):
						if(i != count_data_root1 ):
							sample = PurePosixPath(unquote(urlparse(data_root1).path)).parts[i]
							index[i - 1].add(sample)

							#print(f"{YELLOW}: {index[i-1]}{RESET}")


					#print(index)
		            #array_root_de[count_data_root1 - 3].append(index)
		            #temp = []
		            #temp.append(index)
		            #print(temp)
					temp.append(list(index))



			temp.sort(reverse=True, key=myFunc)

			#for data in temp:
				#print(data)
		                  

			chee = []
			for data in temp:
				chee.append(str(data[1]))

			
			#unique(chee)
			return temp




#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
		def ___get_topics__(categories):
			obj = 0
			check = 0
			while( (obj <= 0) | (obj > len(categories)) ):
				obj = int(input("Enter number to select category)"))
				check = obj
				break
			
			array_category = []
			#categories[i][0] = href
			#categories[i][1] = title
			array_category.append((categories[check - 1][0], categories[check - 1 ][1]))

			return array_category




		def __create_dirPath__(categories):
			for href, title in categories:
				dirPath_html = "{}/{}/{}_html".format(self.parsedUrl.hostname, title, title)	
				dirPath_word = "{}/{}/{}_word".format(self.parsedUrl.hostname, title, title)
				dirPath_BoW =  "{}/{}/{}_BoW".format(self.parsedUrl.hostname, title, title)
				dirPath_Tf_Idf = "{}/{}/{}_Tf_Idf".format(self.parsedUrl.hostname, title, title)
				dirPath_Cosine = "{}/{}/{}_Cosine".format(self.parsedUrl.hostname, title, title)
				dirPath_Precision = "{}/{}/{}_Precision".format(self.parsedUrl.hostname, title, title)
				dirPath_Recall = "{}/{}/{}_Recall".format(self.parsedUrl.hostname, title, title)
				dirPath_F_score = "{}/{}/{}_Fscore".format(self.parsedUrl.hostname, title, title)
				os.makedirs(dirPath_html, exist_ok=True)
				os.makedirs(dirPath_word, exist_ok=True)
				os.makedirs(dirPath_BoW, exist_ok=True)
				os.makedirs(dirPath_Tf_Idf, exist_ok=True)
				os.makedirs(dirPath_Cosine, exist_ok=True)
				os.makedirs(dirPath_Precision, exist_ok=True)
				os.makedirs(dirPath_Recall, exist_ok=True)
				os.makedirs(dirPath_F_score, exist_ok=True)


				#create dirPath Bow and TF-IDF inside Cosine
				dirPath_Cosine_BoW = "{}/{}/{}_Cosine/{}".format(self.parsedUrl.hostname, title, title,"BoW")
				dirPath_Cosine_Tf_Idf = "{}/{}/{}_Cosine/{}".format(self.parsedUrl.hostname, title, title, "Tf_Idf")
				os.makedirs(dirPath_Cosine_BoW, exist_ok=True)
				os.makedirs(dirPath_Cosine_Tf_Idf, exist_ok=True)



		ps = PorterStemmer()
		    
		corpus = [] 

		categories = None
		categories, error = __get_categories__(self.url,self.response,  self.supportCategories)


		__show_topics__(categories)
		array_categories = ___get_topics__(categories)

		print(str(array_categories))
		__create_dirPath__(array_categories)


		array_Travel = [
		'https://edition.cnn.com/entertainment/culture/',
		'https://edition.cnn.com/entertainment/movies/',
		'https://edition.cnn.com/entertainment/celebrities/',
		'https://edition.cnn.com/entertainment/tv-shows/']

		temp = []
		temp_de = []
		for href, title in array_categories:
			temp.append(title)
			temp_de.append(href)

		print(str(temp[0]))
		print(str(temp_de[0]))


		result = []
		result = __show_elements_topics__(str(temp_de[0]))
		#__show_hylt__(result)


		result_de = []
		result_de = __hylt__(result, str(temp_de[0]))
		rere = []
		rere = unique(result_de)
		#for data in result_de:
			#print(str(data))

		result_de_de = []
		result_de_de = __url_hylt__(array_Travel, str(urlparse(temp_de[0]).netloc))
		#result_de_de = __url_hylt__(array_Travel, str(temp_de[0]))


		


		dirPath_html_Travel = "{}/{}/{}_html".format(self.parsedUrl.hostname,temp[0], temp[0])








		for i in range(len(result_de_de)):

			yield scrapy.Request(url=result_de_de[i],meta={'folder_pat':dirPath_html_Travel}, callback=self.parse)






#=============================Make Directoy==================================================#
		



		array_name_file = []
		array_file = []
		dirPath_html = "{}/{}/{}_html".format(self.parsedUrl.hostname,str(temp[0]), str(temp[0]))	
		for root, dirs, files in os.walk(dirPath_html):
			for file in files:
				if file.endswith(".txt"):
					#print(os.path.join(file).split(".txt"))
					#print(os.path.join(root, file)
					array_sample = []
					array_sample = os.path.join(file).split(".txt")
						
					array_file.append(os.path.join(file))

					array_name_file.append(array_sample[0])


		for data in array_name_file:
			print(str(data))



		#dirPath_html = "{}/{}/{}_html".format(self.parsedUrl.hostname, title, title)	
		dirPath_word = "{}/{}/{}_word".format(self.parsedUrl.hostname,str(temp[0]), str(temp[0]))
		dirPath_BoW = "{}/{}/{}_BoW".format(self.parsedUrl.hostname, str(temp[0]), str(temp[0]))
		dirPath_Tf_Idf = "{}/{}/{}_Tf_Idf".format(self.parsedUrl.hostname, str(temp[0]), str(temp[0]))
		dirPath_Cosine = "{}/{}/{}_Cosine".format(self.parsedUrl.hostname, str(temp[0]), str(temp[0]))


		dirPath_Cosine_BoW = "{}/{}/{}_Cosine/{}".format(self.parsedUrl.hostname, str(temp[0]), str(temp[0]),"BoW")
		dirPath_Cosine_Tf_Idf = "{}/{}/{}_Cosine/{}".format(self.parsedUrl.hostname, str(temp[0]), str(temp[0]),"Tf_Idf")

		luachon = 1

		if(luachon == 1):
			for data in array_file:
				text = __get_text__("{}/{}".format(dirPath_html, data))
				text_cleaned = __clean_html__(text)

				#print(str(text_cleaned))
				sents = sent_tokenize(text_cleaned)

				#print(str(sents))

				sents_cleaned = [__remove_special_character(s) for s in sents]
				text_sents_join = ' '.join(sents_cleaned)
				words = word_tokenize(text_sents_join)
				words = [word.lower() for word in words]
				words = [word for word in words if word not in self.my_stopwords]
				ps = PorterStemmer()
				words = [ps.stem(word) for word in words]
				stringwords = ' '.join(words)

				sample = ''
				for i in words:
					sample += i 
					sample += " "
				#print(str(stringwords))
				writeText("{}/{}".format(dirPath_word, data), stringwords)



		
			for data1 in array_file:
				text = __get_text__("{}/{}".format(dirPath_word, data1))
				corpus_final =[]
				corpus_final.append(text)
				result = CountVectorizer()
				bow = result.fit_transform(corpus_final).todense()

				bow1 = result.vocabulary_

				writeCountVectorizer(bow, bow1, data1, dirPath_BoW)


		
			for data2 in array_file:
				text = __get_text__("{}/{}".format(dirPath_word, data2))
				corpus_final =[]
				corpus_final.append(text)	

				tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
				tf_idf_matrix = tf.fit_transform(corpus_final)
				feature_names = tf.get_feature_names()
				dense = tf_idf_matrix.todense()

				writeTfidfVectorizer(tf_idf_matrix, feature_names, dense, data2, dirPath_Tf_Idf )



		
			for data3 in array_file:
				
			
				text = __get_text__("{}/{}".format(dirPath_word, data3))
				corpus_final =[]
				corpus_final.append(text)

				result = CountVectorizer()
				bow = result.fit_transform(corpus_final).todense()

				bow1 = result.vocabulary_


				tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
				tf_idf_matrix = tf.fit_transform(corpus_final)
				feature_names = tf.get_feature_names()
				dense = tf_idf_matrix.todense()


				corpus_final_BoW = []
				corpus_final_Tf = []
				corpus_final_BoW = CosiSim(bow)
				corpus_final_Tf = CosiSim(dense)

				outout(corpus_final_BoW, data3, dirPath_Cosine_BoW)
				outout(corpus_final_Tf, data3, dirPath_Cosine_Tf_Idf)
				



		elif(luachon == 2):
			for data4 in array_file:
				text = __get_text__("{}/{}".format(dirPath_word, data4))
				corpus_final = []
				corpus_final.append(text)

				iris = datasets.load_iris()
				x = iris.data
				y = iris.target
				class_names = iris.target_names

				x_train, x_test, y_train, y_test = train_test_split(x, y,  random_state = 0, test_size = 0.3)
				knn = KNeighborsClassifier(n_neighbors = 10)
				knn.fit(x_train, y_train)

				accuracy = knn.score(x_test, y_test)
				y_pred = knn.predict(x_test)
				cm = confusion_matrix(y_test, y_pred)
				precision_score(y_test, y_pred, average=None)
				recall_score(y_test, y_pred, average=None)
				f1_score(y_test, y_pred, average=None)
				classifier = svm.SVC(kernel='linear', c=0.01).fit(x_train, y_train)

				np.set_printoptions(precison=2)
				titles_options = [("Confusion matrix, without normalization", None), ]
				for title, normalize in titles_options:
					disp = plot_confusion_matrix(classifier, x_test, y_test)

