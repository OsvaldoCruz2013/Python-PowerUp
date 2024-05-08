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
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")



    #Entrar no sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


    # aqui pode ser que ele demora alguns segundos para carregar o site

time.sleep(3)

2. # Fazer login no sistema
   #print(pyautogui.position())

pyautogui.click(x=804, y=507)
pyautogui.write("Aulapython@gmail.com")#escreve o email

pyautogui.press("tab") #passou para o campo de senha

pyautogui.write("123456")#escreve a senha

pyautogui.press("tab") #passou para o campo de login

pyautogui.press("enter")#login
