import requests
#import pdb;pdb.set_trace()
from bs4 import BeautifulSoup
############################################################################
                           # Criacao De web Sraping 


                           #Variaveis Gerais

casaDosDados = 'https://casadosdados.com.br/solucao/cnpj?q=2'

wh = 'https://web.whatsapp.com/'

page = requests.get('https://tecnoguia.istocks.club/7-dicas-para-personalizar-a-aparencia-do-seu-terminal-linux/2021-08-01/')#('https://www.webscraper.io/test-sites/e-commerce/allinone')


##############################################################################
                          # Campos De Funções

def link():
    for link in soup.find_all("a"):
        print(link.get("href" ,""))

if page.status_code == 200:
    soup =  BeautifulSoup(page.text)
    link()



else :
    print('deu errado')








    
