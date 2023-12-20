# Enter script code
import tkinter as tk
#from import tkinter *
from tkinter import *


import pyautogui as bot
import time
#import webbrowser as web


#https://lista.mercadolivre.com.br/kit-arduino#D[A:kit%20arduino]
# Abrir Varias Paginas no Navegador 

#break_count = 0

#web.open("https://bubble.io/page?name=index&id=viverbemseguroscrm&tab=tabs-1")
#time.sleep=(15)

#web.open_new("https://shopee.com.br")

#Chrome('google-chrome')

    


# abrir Um arquivo
with open("aa.csv") as f:
    next(f)
    
    
    for line in (f):
        line=line.strip()
        line=line.split(",")
        print("Dados De teste Automação denner:",line)
        
        nome=line[0]
        telefone=line[1]
        tipoDeEquipe=line[2]


         #Clicar no cammpo indenficador por imagem sem precisa da posicao  
    bot.click(bot.locateCenterOnScreen("nome.png",confidence=0.8),duration=1)
    bot.typewrite(nome,interval=0.20)


    bot.click(bot.locateCenterOnScreen("telefone.png",confidence=0.8),duration=1)
    bot.typewrite(telefone,interval=0.10)
 

    bot.click(bot.locateCenterOnScreen("tipoDeEquipe.png",confidence=0.8),duration=1)
    bot.typewrite(tipoDeEquipe,interval=0.10)

    bot.click(bot.locateCenterOnScreen("salvar.png",confidence=0.8),duration=1)
    bot.click(interval=0.1)




    print(f"Atenção denner Esta Sendo tirado print Agora do cadastro")

    bot.screenshot(f"cadastro_(nome).png")
     

    time.sleep(1)


bot.alert(text="Automação Finalizada ", title="Aviso Da Automação", button="ok")
bot.alert(text='a', title='s', button='OK')