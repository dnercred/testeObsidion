

# Enter script code
import tkinter as tk
#from import tkinter *
from tkinter import *


import pyautogui as bot
#biblioteca de Tempo
import time
import webbrowser as web


# Variavel dos sites pra abrir
bubble=[ #index ViverBem seguros Bubble
       "https://bubble.io/page?name=index&id=viverbemseguroscrm&tab=tabs-1",
         # Pagina Inicial Versão live
       "https://www.sistemaviverbemseguros.com",
         # Banco de Dados 
       "https://bubble.io/page?name=index&id=viverbemseguroscrm&tab=tabs-3&subtab=Data+Types&type_id=afazeres",
                


time.sleep(1)

# Abrir Varias Paginas no Navegador 
  # Obs looper com parametro do abrir navegador 
for b in bubble:
    web.open_new(b)

time.sleep=(10)




bot.click(bot.locateCenterOnScreen("abaViverBem.png",confidence=0.8),duration=0.25)
bot.click(interval=2)
 # Esperar 1 seg
time.sleep(1)

with bot.hold('win'):
        bot.press(['left'])




"""bot.click(bot.locateCenterOnScreen("ligardepois.png",confidence=0.8),duration=0.25)
 # Esperar 1 seg
time.sleep(1)




bot.press('up')
time.sleep(0.25)

bot.press('up')
time.sleep(0.25)

bot.press('up')
time.sleep(0.25)

bot.press('up')
time.sleep(0.25)

bot.press('up')
time.sleep(0.25)

 
bot.click(interval=2)


print("Bot acabou de Clicar Em modificar Etiqueta ")



print("Bot Informa ja Acabei meu trabalhado blz 😀")  


with bot.hold('win'):
        bot.press(['left'])

#bot.click(bot.locateCenterOnScreen("vazio.png",confidence=0.8),duration=5)
# 

bot.click(bot.locateCenterOnScreen("tipoDeEquipe.png",confidence=0.8),duration=1)
bot.typewrite(tipoDeEquipe,interval=0.10)

bot.click(bot.locateCenterOnScreen("salvar.png",confidence=0.8),duration=1)
bot.click(interval=0.1)




    #print(f"Atenção denner Esta Sendo tirado print Agora do cadastro")

    #bot.screenshot(f"cadastro_(nome).png")"""
     

#time.sleep(1)


#bot.alert(text="Automação Finalizada ", title="Aviso Importante sobre  Automação", button="ok")"""
