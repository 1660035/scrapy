from pyquery import PyQuery
import requests
import re
import os
from urllib import parse as UrlParser
from bs4 import BeautifulSoup
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
my_stopwords = set(stopwords.words('english') + list(punctuation))

supportCategories = [
    'giáo dục',
    'y tế',
    'khoa học - công nghệ',
    'giải trí',
    'thể thao',
    'sức khỏe',
    'đời sống',
    'du lịch'
]
supportCategories = [re.sub(r"\s|-", '', category)
                     for category in supportCategories]

##


def writeText(path, content):
    file = open(path, "w", encoding="utf-8")
    if isinstance(content, str):
        file.write(content)
    elif (isinstance(content, collections.abc.Iterable)):
        for item in content:
            file.write(item + '\n')

    file.close()

##


def getCategories(url, supportCategories):
    parsedUrl = UrlParser.urlparse(url)

    response = requests.get(url)
    if response.status_code != 200:
        return None, 'status code is not 200'

    response.encoding = 'utf8'
    doc = PyQuery(response.text)

    allLinks = doc('a[href]')

    processedLink = {}
    categories = []
    for link in allLinks:
        link = doc(link)
        href = link.attr('href')
        parsedHref = UrlParser.urlparse(href)
        if not bool(parsedHref.hostname):
            href = "{}://{}{}".format(parsedUrl.scheme,
                                      parsedUrl.hostname, href)

        href = re.sub(r"\/+$", '', href)
        if href in processedLink:
            continue

        processedLink[href] = True

        title = link.text().strip()
        title_ = title.lower()
        title_ = re.sub(r"\s|-", '', title_)

        if title_ in supportCategories:
            categories.append((href, title))

    return categories, None

##


def analyzeLink(href, linksDict):
    response = requests.get(href)
    if response.status_code == 200:
        response.encoding = 'utf8'
        doc = PyQuery(response.text)
        allLinks = doc('a[href]')

        linksDict__ = {}
        for link in allLinks:
            link = doc(link)
            title = link.text().strip()
            href = link.attr('href')
            if href not in linksDict__ and len(title) > 0:
                linksDict__[href] = {
                    'href': href,
                    'title': title
                }

                if href not in linksDict:
                    linksDict[href] = {
                        'href': href,
                        'title': title,
                        'count': 1
                    }
                else:
                    linksDict[href]['count'] += 1


##
def getCategoriesAuto(doc):
    allLinks = doc('a[href]')

    linksDict = {}
    for link in allLinks:
        link = doc(link)
        title = link.text().strip()
        href = link.attr('href')
        if href not in linksDict and len(title) > 0:
            linksDict[href] = {
                'href': href,
                'title': title,
                'count': 1
            }

    hrefs = list(linksDict.keys())[:10]

    for href in hrefs:
        analyzeLink(href, linksDict)

    categories = []
    for href in linksDict:
        data = linksDict[href]
        count = data['count']
        href = data['href']
        title = data['title']
        words = re.split(r"\s", title)
        wordsCount = len(words)
        if count >= 7 and wordsCount <= 6:
            categories.append({
                'href': href,
                'title': title
            })

    return categories


##
def get_text(file):
    read_file = open(file, "r", encoding="utf8")
    text = read_file.readlines()
    text = ' '.join(text)
    return text

def clean_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

def remove_specical_character(text):
    string = re.sub('[^\w\s]','',text)
    string = re.sub('\s+',' ',string)
    string = string.strip()
    return string

def entry():
    url = input("Input website's url: ")
    if not bool(url):
        url = 'https://tuoitre.vn/'

    categories = None

    while True:
        categories, error = getCategories(url, supportCategories)

        if error != None:
            print(error)
            url = input("Input another website's url: ")
            if not bool(url):
                url = 'https://tuoitre.vn/'
        else:
            break

    selectedCategories = []
    input("Enter y (yes) to select category, another to skip (enter to continue)")
    for href, title in categories:
        print("Category: {}, link: {}".format(title, href))
        userInput = input("Select {}? ".format(title))
        yesInputs = ["y", "Y"]
        if userInput in yesInputs:
            selectedCategories.append((href, title))

    parsedUrl = UrlParser.urlparse(url)
    for href, title in selectedCategories:
        response = requests.get(href)
        if response.status_code == 200:
            response.encoding = 'utf8'
            html = response.text
            dirPath = "output_html/{}/{}".format(parsedUrl.hostname, title)
            os.makedirs(dirPath, exist_ok=True)
            writeText("{}/{}.txt".format(dirPath, title), html)
            
            dirPathWord = "output_word/{}_word/{}_word".format(parsedUrl.hostname, title)
            os.makedirs(dirPathWord, exist_ok=True)
            text = get_text("{}/{}.txt".format(dirPath, title))
            text_cleaned = clean_html(text)
            sents = sent_tokenize(text_cleaned)
            sents_cleaned = [remove_specical_character(s) for s in sents]
            text_sents_join = ''.join(sents_cleaned)
            words = word_tokenize(text_sents_join)
            words = [word.lower() for word in words]
            words = [word for word in words if word not in my_stopwords]
            ps = PorterStemmer()
            words = [ps.stem(word) for word in words]
            stringwords = ' '.join(words)
            writeText("{}/{}_word.txt".format(dirPathWord, title), stringwords)

    print('done')


entry()


"""
    response = requests.get('https://www.news.com.au/sport/cycling/most-awkward-moment-of-lance-armstrongs-30-for-30-documentary/news-story/dfaf55f27e638a977f65905eb4506645')
    response.encoding = 'utf8'
    html = response.text
    
    print(str(html))    
"""