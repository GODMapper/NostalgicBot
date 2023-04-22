# del = start the bot
# esc = pause the bot

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
        for i in range(10):
            #TODO add region
            minimapWindow = 3435, 33, 106, 107
            flag_position = pyautogui.locateOnScreen(item['path'],region=minimapWindow)
            if flag_position == None:
                return
            self.actions.move_and_click(flag_position)
            sleep(item['wait'])

    def start_route(self):
        while self.isStarted:
            for item in self.infos:
                self.go_to_flag(item)
                sleep(1)
                
    def target_key(self,key):
        print(key)
        if key == keyboard.Key.esc:
            return False
        if key == keyboard.Key.delete:
            threading.Thread(target=self.start_route).start()

    def start_keyboard(self):
        with Listener(on_press=self.target_key) as listener:
            listener.join()

hunt = Walker()
hunt.start_keyboard()    