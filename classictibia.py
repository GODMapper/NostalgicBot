import pyautogui
import pathlib
import time


# Set pyautogui functions to zero delay isabelle
pyautogui.PAUSE = 0

# Disable the pyautogui failsafe 
pyautogui.FAILSAFE = False


# Paths
currentPath = pathlib.Path(__file__).parent.resolve()
monstersPath = f'{currentPath}/src/images/monsters/'
barsPath = f'{currentPath}/src/images/bars/'
containersPath = f'{currentPath}/src/images/containers/'
lootsPath = f'{currentPath}/src/images/loots/'


# Coordinates
#left, top, width, height
gameWindow = 1680, 0, 1920, 1080
# TODO Battle window need to be resized to minimum size
battleWindow = 3425, 372, 175, 172
barsWindow = 3430, 145, 150, 35
backpackWindow = 3425, 542, 175, 215


#Until now, all functions were tested under controlled ambients, deeper tests are needed
# Functions
def manaTrainer():
    mana = pyautogui.locateOnScreen(f"{barsPath}mana.png", region=barsWindow)
    if mana is not None:
        # TODO Not necessary anymore fix 
        pyautogui.moveTo(3333, 475)
        time.sleep(1)
        pyautogui.click(3333, 475)
        time.sleep(1)
        pyautogui.press('f1')
        time.sleep(1)

def getTarget():
    # Locating targets os screen
    swampTroll = pyautogui.locateOnScreen(f"{monstersPath}swamptroll.png", region=battleWindow)
    swampTrollTargeted = pyautogui.locateOnScreen(f"{monstersPath}swamptrolltargeted.png", region=battleWindow)

    # Already have a target do nothing
    if swampTrollTargeted is not None:
        time.sleep(1)
        print("Already have a target.")
    
    # Dont have a target setting one
    elif swampTroll is not None:
        xSwamp, ySwamp = pyautogui.center(swampTroll)
        pyautogui.moveTo(xSwamp, ySwamp)
        pyautogui.click(xSwamp, ySwamp)
        pyautogui.moveTo(3333, 475)
        print("Attacking.")

# Under deployment
def getLoot():
    goldCoin = pyautogui.locateOnScreen(f"{lootsPath}gold.png", region=backpackWindow)
    print(goldCoin)

# Starting bot
def main():
    try:
        while True:
            getTarget()
            manaTrainer()
            # Under Deployment
            # getLoot()
            time.sleep(1)
            continue
    except KeyboardInterrupt:
        raise SystemExit

if __name__ == '__main__':
    main()  

