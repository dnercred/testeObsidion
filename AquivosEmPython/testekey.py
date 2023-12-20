import  keyboard
import pyautogui as bot
import time


def gravar():
    print("digite a")
    keyboard.wait("a")
    
    keyboard.add_hotkey('g',lambda:keyboard.write('pyAutogui'))


print(f"  Chmando a funçaõ gravar")
gravar()



def comandos():
    print('digit ctrl+alt+j')
    #keyboard.
    keyboard.add_hotkey("ctrl+alt+j", lambda: print("comandos"))
    print('gg') 
    
    print(f"  Chamdno a funcao comandos")
comandos()



#from pynput.keyboard import Key, Controller:

    




  



    

   # print('Agora escreva d')
   # keyboard.add_hotkey('d',lambda:keyboard.write('mano denner santos satnso '))
   # print('Vou pra proxima funcao')
   # time.sleep(5)

    
   # keyboard.play(gravacao , speed_factor = 3)
   # time.sleep(4)
   
   #bot.hotkey('ctrl','x')
    #time.sleep(10)
    #keyboard.add_abbreviation("@", "denner.com")

   # print(  "vou finalizar ")
    #time.sleep(3)
    #keyboard.type('Hello Worldfkjlskjladmasdf.mssfdhfdjdgfhjdfghjghjfhjkfhgjn')         
   
