import pyautogui
''' import pyperclip ''' # caso haja caracteres especiais no link a ser colado
import time

pyautogui.PAUSE = 0.5

pyautogui.hotkey("win")
pyautogui.write('firefox')
pyautogui.press('enter')

time.sleep(2)
pyautogui.click(x=309,y=65)
pyautogui.write('https://fallguys-db.pages.dev/')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=690, y=249)

# para instalar o pyautogui -> no terminal do VSCode, digitar pip install pyautogui
# para tornar o código executável -> no terminal do VSCode, digitar pip install pyinstaller
# ainda no terminal, digitar -> pyinstaller --onefile -w db.py
# o -w no código anterior mostra alguma janela que interaja com o usuário, caso contrário
# o código é executado todo em prompt de comando