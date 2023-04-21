import pyautogui
import pathlib
import time


# Set pyautogui functions to zero delay
pyautogui.PAUSE = 0

# Disable the pyautogui failsafe 
pyautogui.FAILSAFE


# Paths
currentPath = pathlib.Path(__file__).parent.resolve()
monstersPath = f'{currentPath}/src/images/monsters/'
barsPath = f'{currentPath}/src/images/bars/'


# Coordinates
gameWindow = 1680, 0, 1920, 1080
battleWindow = 3425, 372, 175, 172
barsWindow = 3430, 145, 150, 35


# Functions
# TODO Need to be activated
def manaTrainer():
    mana = pyautogui.locateOnScreen(f"{barsPath}mana.png", region=barsWindow)
    if mana is not None:
        pyautogui.moveTo(3333, 475)
        time.sleep(1)
        pyautogui.click(3333, 475)
        time.sleep(1)
        pyautogui.press('f1')
        time.sleep(1)

#TODO Need tests under production
def getTarget():
    swampTroll = pyautogui.locateOnScreen(f"{monstersPath}swamptroll.png", region=battleWindow)
    swampTrollTargeted = pyautogui.locateOnScreen(f"{monstersPath}swamptrolltargeted.png", region=battleWindow)

    if swampTrollTargeted is not None:
        time.sleep(1)
        print("Already have a target.")
    
    elif swampTroll is not None:
        xSwamp, ySwamp = pyautogui.center(swampTroll)
        pyautogui.moveTo(xSwamp, ySwamp)
        pyautogui.click(xSwamp, ySwamp)
        pyautogui.moveTo(3333, 475)
        print("Attacking.")

    targeting = getTarget()
    try:
        targeting
        while True:
            time.sleep(1)
            print("sleep")
            continue
    except KeyboardInterrupt:
        raise SystemExit

#TODO Create the main function
if __name__ == '__main__':
    getTarget()