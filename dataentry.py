import pyautogui,pyperclip,time


text  = pyperclip.paste()
mytext = text.strip()

names = mytext.split('&nbsp;&nbsp;&nbsp;&nbsp;')
time.sleep(5)
for name in names :
    pyautogui.typewrite(name)
    pyautogui.press('tab')

