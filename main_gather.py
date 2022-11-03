import pyautogui
import time
import webbrowser


s = """https://play.pixels.xyz/farm3425"""
s = s.split('\n') 

def hold_W (nums):
    for i in range(nums):
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")

def hold_S (nums):
    for i in range(nums):
        pyautogui.keyDown("s")
        pyautogui.keyUp("s")


cycler = 0
while cycler != 3:
	for i in range(200):
		time.sleep(10)
		pyautogui.moveTo(100, 100)
		if len(list(pyautogui.locateAllOnScreen("soil.png"))) > 4:
			pyautogui.moveTo(pyautogui.size()[0]/2 +140, pyautogui.size()[1]/2)
			pyautogui.click()
			break
		while 1:
			if pyautogui.locateOnScreen("carrot_2.png") != None:
				break
		hold_S(6)
		pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2)
		pyautogui.press("num1")
		for i in range(20):
			pyautogui.click()
		pyautogui.press("num6")
		soil_locations = list(pyautogui.locateAllOnScreen('carrot_2.png'))
		for i in range(len(soil_locations)):
			pyautogui.moveTo(soil_locations[i][0], soil_locations[i][1])
			pyautogui.click()
			time.sleep(0.1)
				
		pyautogui.press("num6")
		pyautogui.moveTo(pyautogui.size()[0]/2 +140, pyautogui.size()[1]/2 -140)
		pyautogui.click()
		if i == 199:
			cycler = 3
