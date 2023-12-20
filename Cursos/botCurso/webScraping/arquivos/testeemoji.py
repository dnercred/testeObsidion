





import requests ,bs4

#url='https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
#from requests import get
#from bs4 import BeautifulSoup

#import pandas as pd
#import numpy as np

import time
import re

url = 'https://unicode.org/emoji/charts/full-emoji-list.html'

#response2 = requests.get(url2)

reponse = requests.get(url)
print(reponse.content)
##print(response.content)
#:wq!print(response.json())


