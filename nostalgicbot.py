# Welcome to NostalgicBot by Thiago Medeiros!
# del = start walker
# end = start targeting
# page down = start manatrainer
# esc = pause bot

import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
import threading
import json
from actions import *
from time import sleep
from config import *

class Walker:
    def __init__(self):
        self.isStarted = True
        with open(f'{targetName}/{targetName}.json', 'r') as file:
            infos = file.read()
        self.infos = json.loads(infos)
        self.actions = Actions()

    def go_to_flag(self, item):
        while True:
            swampTroll = pyautogui.locateOnScreen(f"{monstersPath}swamptroll.png", confidence=0.8, region=battleWindow)
            swampTrollTargeted = pyautogui.locateOnScreen(f"{monstersPath}swamptrolltargeted.png", confidence=0.8, region=battleWindow)
            if swampTroll or swampTrollTargeted:
                print("Tem swamp na tela, aguardando...")
                sleep(5)
            else:
                print("Sem swamp na tela, indo para o waypoint...")
                flag_position = pyautogui.locateOnScreen(item['path'], confidence=0.7, region=miniMap)
                if flag_position:
                    print("Flag encontrada")
                    self.actions.move_and_click(flag_position)
                    pyautogui.moveTo(3333, 475)
                    sleep(item['wait'])
                else:
                    print("Flag não encontrada na tela. Aguardando..")
                    sleep(1)
                    return

    def start_route(self):
        while self.isStarted:
            for item in self.infos:
                self.go_to_flag(item)
                sleep(1)

    def getTarget(self):
        while self.isStarted:
            swampTroll = pyautogui.locateOnScreen(f"{monstersPath}swamptroll.png", confidence=0.8, region=battleWindow)
            swampTrollTargeted = pyautogui.locateOnScreen(f"{monstersPath}swamptrolltargeted.png", confidence=0.8, region=battleWindow)
            if swampTrollTargeted:
                sleep(1)
            elif swampTroll:
                xSwamp, ySwamp = pyautogui.center(swampTroll)
                pyautogui.moveTo(xSwamp, ySwamp)
                pyautogui.click(xSwamp, ySwamp)
                pyautogui.moveTo(3333, 475)

    def manaTrainer(self):
        while self.isStarted:
            mana = pyautogui.locateOnScreen(f"{barsPath}mana.png", region=barsWindow)
            if mana:
                pyautogui.moveTo(3333, 475)
                sleep(1)
                pyautogui.click(3333, 475)
                sleep(1)
                pyautogui.press('f1')
                sleep(1)

    def eatFood(self):
        while True:
            food = pyautogui.locateOnScreen(f"{lootsPath}fish.png", region=lootWindow)
            if food:
                xFood, yFood = pyautogui.center(food)
                pyautogui.moveTo(xFood, yFood)
                pyautogui.rightClick(xFood, yFood)
                pyautogui.moveTo(3333, 475)
    
    def target_key(self,key):
        print(key)
        if key == keyboard.Key.esc:
            print("Bot Stopped.")
            return False
        if key == keyboard.Key.delete:
            print("Walker ON.")
            threading.Thread(target=self.start_route).start()
        if key == keyboard.Key.end:
            print("Targetting ON")
            threading.Thread(target=self.getTarget).start()
        if key == keyboard.Key.page_down:
            print("Mana Trainer ON")
            threading.Thread(target=self.manaTrainer).start()
        if key == keyboard.Key.insert:
            print("EatFood ON")
            threading.Thread(target=self.eatFood).start()

    def start_keyboard(self):
        with Listener(on_press=self.target_key) as listener:
            listener.join()

hunt = Walker()
hunt.start_keyboard()    