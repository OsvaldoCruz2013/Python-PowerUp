# Python-PowerUp
#Aprendendo python com o hathasg treinamentos

#Utilizando as bibliotecas

import pyautogui

import time

#Para ter uma pausa antes de prosseguir para o proximo passo

pyautogui.PAUSE 

#Abrir o navegador

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

