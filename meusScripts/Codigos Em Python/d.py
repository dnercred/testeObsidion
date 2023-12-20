
#from bs4 import BeautifulSoup
  

#soup = BeautifulSoup(markup, 'html.parser')
  
#finding the div with the id
#div_bs4 = soup.find('div', id = "_21Ahp")
  
#print(div_bs4.string)
#soup = BeautifulSoup(html_page, 'html.parser')
#soup.prettify()


#for link in soup.find_all('a'):
from urllib.request import urlopen

from bs4 import BeautifulSoup as bs
import requests

html = urlopen("https://www.sistemaviverbemseguros.com/version-test/tabelinha")
res = bs.soup.find('a').text
print(res) 

#   print(link.get('https://medium.com/pyladiesbh/beautiful-soup-parseamento-de-html-337197a7d4b9'))
