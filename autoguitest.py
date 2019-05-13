import pyautogui

buttonAlocation = pyautogui.locateOnScreen('a.png')
print("Button A:" , buttonAlocation)

buttonSlocation = pyautogui.locateOnScreen('s.png')
print("Button S:" , buttonSlocation)

buttonDlocation = pyautogui.locateOnScreen('d.png')
print("Button D:" , buttonDlocation)

buttonFlocation = pyautogui.locateOnScreen('f.png')
print("Button F:" , buttonFlocation)



pyautogui.moveTo('f.png') 
pyautogui.click('f.png') 
