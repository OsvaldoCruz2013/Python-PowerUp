import pyautogui
import time
pyautogui.PAUSE = 0.5


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#print(pyautogui.position())
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
#print(pyautogui.position())
pyautogui.click(x=899, y=442)
pyautogui.write("Aulapython@gmail.com")#escreve o email

pyautogui.press("tab") #passou para o campo de senha

pyautogui.write("123456")#escreve a senha

pyautogui.press("tab") #passou para o campo de login

pyautogui.press("enter")#login

time.sleep(5)

#print(pyautogui.position())














