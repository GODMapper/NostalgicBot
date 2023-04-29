import pyautogui
from time import sleep
from config import *

class Actions:
    def __init__(self):
        pass
    
    def move(self, imagem_position):
        x, y = pyautogui.center(imagem_position)
        pyautogui.moveTo(x, y, 0.1)

    def move_and_click(self, imagem_position):
        self.move(imagem_position)
        pyautogui.click()

    def openCorpse(self):
        deadSwampTroll = pyautogui.locateOnScreen(f"{corpsesPath}dead_swamptroll.png", confidence=0.8, region=lootRange)
        if deadSwampTroll:
            xdeadSwamp, ydeadSwamp = pyautogui.center(deadSwampTroll)
            pyautogui.moveTo(xdeadSwamp, ydeadSwamp)
            pyautogui.rightClick(xdeadSwamp, ydeadSwamp)
            pyautogui.moveTo(3333, 475)

# Actions().openCorpse()