import requests
import urllib.request
import re
import json
from ftfy import fix_encoding
from bs4 import BeautifulSoup

import unicodedata
from unidecode import unidecode
def filt(word):
    return unicodedata.normalize('NFKD', word).encode('ascii', errors='ignore').decode('ascii')



htmlText = urllib.request.urlopen("https://vov.vn/api/comments.json?v=1591595725167&action=get&id=711714&page=1")

data = json.load(htmlText)



print (data["comments"])


array = []
array = data["comments"]
print(str(array[0]['Comment']))




payload = {'page': 2, 'count':25}
url = 'https://vov.vn/van-hoa/nghe-si/hong-diem-dong-it-phim-la-loi-the-cua-toi-1055891.vov'





r = requests.get('https://vov.vn/van-hoa/nghe-si/hong-diem-dong-it-phim-la-loi-the-cua-toi-1055891.vov')
print(r.headers)





if r.status_code == 200:
    print('Success!')
elif r.status_code == 404:
    print('Not Found.')












#print (htmlText.decode('utf-8'))