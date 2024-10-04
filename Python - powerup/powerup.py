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
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(1)

#Biblioteca pyautogui
    #import pyautoguimarca  tipo
        #pyautogui.click -> clicar com um mouse

#2-Fazer login
pyautogui.click(x=297, y=357)
pyautogui.write("lukasnunes09@gmail.com")

pyautogui.press("tab")
pyautogui.write("senha123")

pyautogui.press("tab")
pyautogui.press("enter")

#3-Abrir/importar a base de dados de produtos para cadastrar
#pip install pandas numpy openpyxl
import pandas as pd

df = pd.read_csv("produtos.csv")

print(df)

#4=Cadastrar um produto

for linha in df.index:
    #codigo
    codigo = str(df.loc[linha, "codigo"])
    pyautogui.click(x=254, y=257)
    pyautogui.write(codigo)
    
    #marca
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "marca"]))
    
    #tipo
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "tipo"]))

    #categoria
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "categoria"]))

    #preço
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "preco_unitario"]))

    #custo
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "custo"]))

    #Obs
    pyautogui.press("tab")
    obs = str(df.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs) 

    #Apertar o botão
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

#5-Repetir isso tudo até acabar a lista de produtos