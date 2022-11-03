import pyautogui
import time
import webbrowser


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
		time.sleep(11)
		pyautogui.moveTo(100, 100)
		"""if len(list(pyautogui.locateAllOnScreen('empty_slot.png')))+len(list(pyautogui.locateAllOnScreen('empty_slot2.png'))) == 4:
									pyautogui.press('tab')"""
		if pyautogui.locateOnScreen('soil.png') == None:
			pyautogui.moveTo(pyautogui.size()[0]/2 +140, pyautogui.size()[1]/2 )
			pyautogui.click()
			break
		while 1:
			if pyautogui.locateOnScreen("soil.png") != None:
				break
		hold_S(6)
		pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2)
		pyautogui.press("num6")
		for i in range(20):
			pyautogui.click()
		empty = list(pyautogui.locateAllOnScreen('empty_slot.png'))
		pyautogui.press("num" + str(len(empty)+1))
		soil_locations = list(pyautogui.locateAllOnScreen('soil.png'))
		for i in range(len(soil_locations)):
			pyautogui.moveTo(soil_locations[i][0], soil_locations[i][1])
			pyautogui.click()
			time.sleep(0.1)
		pyautogui.press("num5")
		for i in range(len(soil_locations)):
			pyautogui.moveTo(soil_locations[i][0], soil_locations[i][1])
			pyautogui.click()
			time.sleep(0.1)
			
		pyautogui.press("num5")
		pyautogui.moveTo(pyautogui.size()[0]/2 +140, pyautogui.size()[1]/2 -140)
		pyautogui.click()

