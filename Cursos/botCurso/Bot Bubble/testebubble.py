import pyautogui as bot
import time

bot.click(bot.locateCenterOnScreen("home/denner/Área de Trabalho/MundoTech/Cursos/botCurso/Bot Bubble/statusFinanceiro",confidence=0.8),duration=0.25)
bot.click(interval=2)
 # Esperar 1 seg
time.sleep(1)

with bot.hold('win'):
        bot.press(['left'])




#bot.click(bot.locateCenterOnScreen("ligardepois.png",confidence=0.8),duration=0.25)
 # Esperar 1 seg
#time.sleep(1)


