# record.py is used to record waypoints
# Insert - Get photo of flag
# Page Up - Get the coordinates of waypoint
# More information about how to create your own waypoints soon!

import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
import time
import json
from config import *
import os

def create_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

class Recorder:
    def __init__(self):
        self.count = 0
        self.coordinates = []
        create_folder(targetName)

    def photo(self):
        x, y = pyautogui.position()
        screenshot = pyautogui.screenshot(region=(x - 9, y - 9, 15, 15))
        path = f'{targetName}/flag_{self.count}.png'
        screenshot.save(path)
        self.count = self.count +1
        infos = {
            "path": path,
            "wait": 0,
            "start": None
        }
        self.coordinates.append(infos)

    def tick(self):
        last_coordinates = self.coordinates[-1]
        if last_coordinates["start"] is None:
            last_coordinates["start"] = time.time()
        else:
            last_coordinates["wait"] = time.time() - last_coordinates["start"]
            del last_coordinates["start"]

    def key_code(self, key):
        print(key)
        if key == keyboard.Key.esc:
            with open(f'{targetName}/{targetName}.json', 'w') as file:
                file.write(json.dumps(self.coordinates))
            return False
        if key == keyboard.Key.insert:
            self.photo()
        if key == keyboard.Key.page_up:
            self.tick()

    def start(self):
        with Listener(on_press=self.key_code) as listener:
            listener.join()

record = Recorder()
record.start()