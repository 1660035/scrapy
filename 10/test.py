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
import colorama

# init the colorama module
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


total_urls_visited = 0

def unique(list1): 
      
    # insert the list to the set 
    list_set = set(list1) 
    # convert the set to the list 
    unique_list = (list(list_set)) 
    for data in unique_list: 
        print(f"{YELLOW}[*] Internal link: {data}{RESET}")



def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def myFunc(e):
    return len(e)

def get_all_website_links(url):
   
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
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

    print(str(sample_de))



   



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



#get ROOT_2
    for data in array_root_1:
        count_sample = PurePosixPath(
            unquote (
                    urlparse(
                            data
                        ).path
                )
            ).parts
        sample1 = PurePosixPath(
                        unquote (
                                urlparse(
                                        data
                                    ).path
                            )).parts[1]
        count_count = len(count_sample)
        if(count_count >= 3):
            sample2 = PurePosixPath(
                unquote (
                        urlparse(
                                data
                            ).path
                    )).parts[2]
            array_root_2.append((sample1, sample2))


#get ROOT_3 ( IN ROOT_2 )
    for data in array_root_1:
        count_sample = PurePosixPath(
            unquote (
                    urlparse(
                            data
                        ).path
                )
            ).parts

        sample1 = PurePosixPath(
                        unquote (
                                urlparse(
                                        data
                                    ).path
                            )).parts[1]
        count_count = len(count_sample)
        if(count_count >= 4):
            for root1, root2 in array_root_2:
                sample2 = PurePosixPath(
                        unquote (
                                urlparse(
                                        data
                                    ).path
                            )).parts[2]
                if(root2 == sample2):
                    sample3 = PurePosixPath(
                unquote (
                        urlparse(
                                data
                            ).path
                    )).parts[3]
                    array_root_3.append((sample1, sample2, sample3))


    for data in array_root_1:
        count_sample = PurePosixPath(
            unquote (
                        urlparse(
                                data
                            ).path
                    )
                ).parts

        sample1 = PurePosixPath(
                            unquote (
                                    urlparse(
                                            data
                                        ).path
                                )).parts[1]
        count_count = len(count_sample)
        if(count_count >= 5):
            for root1, root2 in array_root_2:
                sample2 = PurePosixPath(
                            unquote (
                                    urlparse(
                                            data
                                        ).path
                                )).parts[2]
                if(root2 == sample2):
                    sample3 = PurePosixPath(
                    unquote (
                            urlparse(
                                    data
                                ).path
                        )).parts[3]


                    array_root_3.append((sample1, sample2, sample3))


            for root1, root2, root3 in array_root_3:
                sample2 = PurePosixPath(
                            unquote (
                                    urlparse(
                                            data
                                        ).path
                                )).parts[2]
                if(root2 == sample2):
                    sample3 = PurePosixPath(
                    unquote (
                            urlparse(
                                    data
                                ).path
                        )).parts[3]
                    if(root3 == sample3):
                        sample4 = PurePosixPath(
                    unquote (
                            urlparse(
                                    data
                                ).path
                        )).parts[4]
                        array_root_4.append((sample1, sample2, sample3, sample4))

#=========    unique(array_root_4)





#get ROOT_4   
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




    print(str(max_count_root))
    check = 2 

    array_root_de = [set() for i in range(max_count_root - 3)]
#lotsosets[0].add('see me?')
    array_root_de[0].add('sdasd')
    array_root_de[1].add('12132')
    temp = []
    print(array_root_de)

    for data_root1 in array_root_1:
        count_data_root1 = len(PurePosixPath(unquote(urlparse(data_root1).path)).parts)
        
        if( count_data_root1 >= 3 ):
            print('--------------------------------------------------------------')

            print(f"{BLUE} {data_root1}{RESET}")
            print(f"{GREEN}: {count_data_root1}{RESET}")

            index = [set() for i in range(count_data_root1 - 1 )]
            print(index)

            for i in range (1, count_data_root1 ):
                if(i != count_data_root1 ):
                    sample = PurePosixPath(unquote(urlparse(data_root1).path)).parts[i]
                    index[i - 1].add(sample)

                    print(f"{YELLOW}: {index[i-1]}{RESET}")


            print(index)
            #array_root_de[count_data_root1 - 3].append(index)
            #temp = []
            #temp.append(index)
            #print(temp)
            temp.append(list(index))



    temp.sort(reverse=True, key=myFunc)

    for data in temp:
        print(data)
                  

    chee = []
    for data in temp:
        chee.append(str(data[1]))

    unique(chee)

    







#===========    unique(array_root_2)
    print("=======================================================================")

#========    unique(array_root_3)
    
    #for data in array_root_2:
        #print(f"{BLUE}[!] Internal link: {data}{RESET}")



            

    #for data in array_root_1:
       # print(f"{GREEN}[!] Internal link: {data}{RESET}")
        #print(str(data))




    return urls


def crawl(url, max_urls=50):
    
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
    #url1 = r"https://www.news.com.au/"
    parser.add_argument("url",  help="The URL to extract links from.")
    parser.add_argument("-m",  "--max_urls", help="Number of max URLs to crawl, default is 30.", default=30, type=int)
    
    args = parser.parse_args()
    url = args.url
    max_urls = (args.max_urls )- 1
    

    crawl(url, max_urls=max_urls)

    print("[+] Total Internal links:", len(internal_urls))
    print("[+] Total External links:", len(external_urls))
    print("[+] Total URLs:", len(external_urls) + len(internal_urls))

    domain_name = urlparse(url).netloc

#test.py -m 50 https://www.news.com.au/

    #for data in internal_urls:
       # print(str(data))
    
    

    #for data in internal_urls:
     #   print(str(data))





    # save the internal links to a file
    #with open(f"{domain_name}_internal_links.txt", "w") as f:
      #  for internal_link in internal_urls:
            #print(internal_link.strip(), file=f)

    # save the external links to a file
   # with open(f"{domain_name}_external_links.txt", "w") as f:
        #for external_link in external_urls:
            #print(external_link.strip(), file=f)