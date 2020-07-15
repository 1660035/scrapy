
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

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()


from urllib.parse import unquote
from pathlib import PurePosixPath


total_urls_visited = 0


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


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
    array_root = []

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

        print(str(href))

    


        count_sample = PurePosixPath(
            unquote (
                    urlparse(
                            href
                        ).path
                )
            ).parts

        count_count = len(count_sample)

        i = 0
     
        for i in range(len(count_sample)):
            sample = PurePosixPath(
            unquote (
                    urlparse(
                            href
                        ).path
                )
            ).parts[i]


            if(sample_de == sample):
                #print(str(sample) + "==============" + str(sample_de))
                print("i=" +str(i ) + "        " + str(sample))






        sample_final = PurePosixPath(unquote(urlparse(href).path)).parts[1]


        if(sample_final == sample_de):
            array_root.append(href)



         

    """

        if not is_valid(href):
            # not a valid URL
            continue
        if href in internal_urls:
            # already in the set
            continue
        if domain_name not in href:
            # external link
            if href not in external_urls:
                #print(f"{GRAY}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue


        
        #print(f"{GREEN}[!] Internal link: {href}{RESET}")





        internal_urls.add(href)


            
        urls.add(href)
        #internal_urls.add(href)

        """
    for data in array_root:
        print(str(data))




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