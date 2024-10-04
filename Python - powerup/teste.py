#passo a passo do projeto
#telefone (21) 99721-8715
#Para instalar a biblioteca: pip install pyautogui no terminal
#Importar pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5


#1-Abrir os sistema do projeto
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

#Abrir o navegador(chrome)
pyautogui.press("win")
pyautogui.write("chrome")   
pyautogui.press("enter")

#Entrar no site do sistema
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Aqui pode ser que ele demore algums segundos para carregar o site
time.sleep(3)