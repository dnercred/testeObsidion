import pyautogui as bot
import time

bot.click(bot.locateCenterOnScreen("/home/denner/Área de Trabalho/MundoTech/Cursos/botCurso/Bot Bubble/statusFinanceiro/statusFinanceiro.png"),duration=0.25)
bot.click(interval=2)
 # Esperar 1 seg
time.sleep(5)



bot.click(bot.locateCenterOnScreen("/home/denner/Área de Trabalho/MundoTech/Cursos/botCurso/Bot Bubble/statusFinanceiro/naoLancados.png"),duration=0.25)
bot.click(interval=2)
# Esperar 1 seg
time.sleep(1)

bot.click(bot.locateCenterOnScreen("/home/denner/Área de Trabalho/MundoTech/Cursos/botCurso/Bot Bubble/statusFinanceiro/tipoDeSala.png"),duration=1)

 # Esperar 1 seg
time.sleep(1)

bot.press(          'entre')
#ot.hotkey('ctrl', 'shift', 'esc')
time.sleep(3)
bot.press("down", presses=6 , interval=0.25)
#bot.press('down',presses=3)
#bot.press('down',presses=3)








#bot.click(bot.locateCenterOnScreen("ligardepois.png",confidence=0.8),duration=0.25)
 # Esperar 1 seg
#time.sleep(1)


