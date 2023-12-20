#!/usr/bin/env python3

import pyautogui as bot
import tkinter as tk
from tkinter import *
import webbrowser as web
####################VARIAVEIS DO PROGRAMA##################
site = ['https://slackjeff.com.br/area-do-aluno/login/index.php','https://web.whatsapp.com/']


##########################################################

for s in site:
    web.open(s)
    print('Acabou'.format(s))
bot.alert(text='FERA')