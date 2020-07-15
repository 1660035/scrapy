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




ps = PorterStemmer()

def main():

	#C:\Users\DELL\Desktop
	#https://tiki.vn/nha-sach-tiki/c8322?src=mega-menu&_lc=Vk4wMzkwMjAwMTU%3D&

	site = input('Nhap url(duong dan) trang web (https://tiki.vn/nha-sach-tiki/c8322?src=mega-menu&_lc=Vk4wMzkwMjAwMTU%3D&): ')
	
	corpus = []
	corpus  = Xuly(site)

	#print(str(corpus))

	corpus_final = []
	corpus_final = filterTexts(corpus)
		
	check = LuaChon()

	if (check == 1):
		o_path = input('Nhap duong dan folder luu file( vd: C:\Users\DELL\Desktop ): ')
		#outputName = input('Nhap ten file xuat ra: ')

		result = CountVectorizer()
		bow = result.fit_transform(corpus_final).todense()

		bow1 = result.vocabulary_

		writeCountVectorizer(bow , bow1, 'BoW', o_path)


	else:
		o_path = input('Nhap duong dan folder luu file( vd: C:\Users\DELL\Desktop ): ')
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
