import newspaper
#https://www.vice.com/en_asia
#http://cnn.com
cnn_paper = newspaper.build('https://www.news.com.au/lifestyle/')



for article in cnn_paper.articles:
	print(str(article.url))
#http://www.cnn.com/2013/11/27/justice/tucson-arizona-captive-girls/
#http://www.cnn.com/2013/12/11/us/texas-teen-dwi-wreck/index.html





#for category in cnn_paper.category_urls():
#	print(category)

#http://lifestyle.cnn.com
#http://cnn.com/world
#http://tech.cnn.com
#...

#cnn_article = cnn_paper.articles[0]
#cnn_article.download()
#cnn_article.parse()
#cnn_article.nlp()

#for category in cnn_paper.category_urls():
	#cat_paper = newspaper.build(category)
	#print (cat_paper.articles) #Gives all articles of category
	#for article in cat_paper.articles:
		#print(article.url) #prints URL for all articles in g