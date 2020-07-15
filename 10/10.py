import os
import re
from bs4 import BeautifulSoup
import nltk
import  shutil
nltk.download('stopwords')
nltk.download('punkt')
from os import  path
import sklearn
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
my_stopwords = set(stopwords.words('english') + list(punctuation))
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

#Ham duyet danh sach file tu thu muc
def browseFiles(path):
	list_path = []
	for (root, dirs, files) in os.walk(path):
		for file in files:
			if file.endswith('.txt'):

				list_path.append(root+"\\"+file)
	return list_path

#Ham doc file xu ly
def readFile(list_path):
	read_files = []
	i = 0
	for i in range (len(list_path)):
		read_file = open(list_path[i], "r", encoding="utf8")
		a = read_file.readlines()
		a = ''.join(a)
		read_file.append(a)
	return read_files

def get_text(file):
	read_file = open(file, "r")
	text = read_file.readlines()
	text = ' '.join(text)
	return text

def write_text(file, words):
	f = open(file, "w")
	for word in words:
		f.write(word)
	f.close()

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

ps = PorterStemmer()
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
		words = [word for word in words if word not in my_stopwords]
		#Chuan hoa tu
		words = [ps.stem(word) for word in words]
		words = ''.join(words)
		res.append(words)
	return res

#Ghi ra file txt
def writeVectorFite(txtAfter, o_path):
	f = open(o_path , 'w+')
	f.write(str(txtAfter))
	f.close


def LuaChon():
    print("1. Phuong phap Bow")
    print("2. Phuong phap TF-IDf")
    doituong = int(input('Nhap phuong phap ban chon :'))

    return doituong



def XuLy3(cor):
    result = CountVectorizer()

    return result
#Main
def main():
	path = input('Nhap duong dan folder can duyet file: ')
	#list_path = browseFiles(path)
	o_path = input('Nhap duong dan folder can xuat ra: ')


	# 	# C:\Users\DELL\Desktop\input.txt
	##C:\Users\DELL\Desktop\output.txt



	f = open(path, "r")
	with f as file:
		text = f.readlines()
		text = ' '.join(text)

	print(str(text))

	text_cleaned = clean_html(text)

	print(str(text_cleaned))
	# tach cau
	sents = sent_tokenize(text_cleaned)
	# Loai bo ky tu dac biet
	sents_cleaned = [remove_special_character(s) for s in sents]
	# Noi cac cau lai thanh text
	text_sents1_join = ' '.join(sents_cleaned)
	# tach tu
	words = word_tokenize(text_sents1_join)
	# dua ve dag chu thhuong
	words = [word.lower() for word in words]
	# loại bo hu tu
	words = [word for word in words if word not in my_stopwords]


	words = [ps.stem(word) for word in words]
	sss = ''
	for i in words:
		sss += i
		sss += " "

	corpus = []
	corpus.append(sss)

	#print(str(corpus))
	#writeVectorFite(corpus, o_path)

	doituongvao = (input('Nhap duong dan thu muc vao :'))
	doituongra = (input('Nhap duong dan thu muc ra :'))

	# C:\Users\DELL\Desktop\input.txt
	##C:\Users\DELL\Desktop\output.txt
	f = open(doituongvao, "r+")
	f_out = open(doituongra, "w+")

	if (LuaChon() == 1):
		print("Lua Chon 1")
		final = XuLy3(f)

		final1 = final.fit_transform(f).todense()
		final2 = final.vocabulary_

		f_out.write(str(final1))
		f_out.write('\n')
		f_out.write(str(final2))

		f.close()

	else:
		print("Lua Chon 2")

		tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
		tf_idf_matrix = tf.fit_transform(f)
		feature_names = tf.get_feature_names()
		dense = tf_idf_matrix.todense()

		final1 = '\n'.join(feature_names)
		final2 = tf_idf_matrix
		final3 = dense

		f_out.write(str(final1))
		f_out.write('\n')

		f_out.write(str(final2))
		f_out.write('\n')

		f_out.write(str(final3))

		f.close()


if __name__ == "__main__":
	main()
