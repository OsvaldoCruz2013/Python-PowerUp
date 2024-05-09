# Passo a Passo do Projeto

1. # Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

    # instalando o pyautogui (pip install pyautogui)
import pyautogui
import time

pyautogui.PAUSE = 0.5
    
    # pyautogui.click -> clicar com o mouse
    # pyautogui.write -> escrever um texto
    # pyautogui.press -> apertar uma tecla no teclado
    # pyautogui.hotkey -> apertar um conjunto de tecla (Crtl + Alt + Del por exemplo)


    #Abrir o navegador(chrome)
pyautogui.press("win")    # apertar a tecla win
pyautogui.write("chrome")    # escrever o nome do navegador
pyautogui.press("enter")    # apertar enter

time.sleep(1)   

    #Entrar no sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


    # aqui pode ser que ele demora alguns segundos para carregar o site

time.sleep(3)   

2. # Fazer login no sistema
#   print(pyautogui.position())

#yautogui.click(x=804, y=507)

pyautogui.click(x=916, y=436)
    
pyautogui.write("Aulapython@gmail.com")#escreve o email

pyautogui.press("tab") #passou para o campo de senha

pyautogui.write("123456")#escreve a senha

pyautogui.press("tab") #passou para o campo de login

pyautogui.press("enter")#login

time.sleep(3)

# 3. Importar a base de dados 
#pip install pandas numpy openpyxl

import pandas as pd

df = pd.read_csv("produtos.csv")

print(df)



for linha in df.index:

    # 4.Cadastrar um produto
    codigo = str(df.loc[linha, "codigo"]) #str = string
    #Clicar no codigo do produto
    pyautogui.click(x=593, y=367)
    #prencher o codigo do produto
    pyautogui.write(codigo)
    #Passar pro proximo campo
    pyautogui.press("tab")
    #Marca
    pyautogui.write(str(df.loc[linha, "marca"]))
    pyautogui.press("tab")
    #Tipo
    pyautogui.write(str(df.loc[linha, "tipo"]))
    pyautogui.press("tab")  
    #Categoria
    pyautogui.write(str(df.loc[linha, "categoria"]))
    pyautogui.press("tab") 
    #Preço
    pyautogui.write(str(df.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #Custo
    pyautogui.write(str(df.loc[linha, "custo"]))
    pyautogui.press("tab")

    #obs
    obs = str(df.loc[linha, "obs"])
    if  obs != "nan":
        pyautogui.write(obs)
        
    #Passar pro proximo campo
    pyautogui.press("tab")
    #Clicar no botão adicionar
    pyautogui.press("enter") 

    #para subir a pagina
    pyautogui.scroll(5000)


