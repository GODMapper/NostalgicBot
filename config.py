import pathlib
import pyautogui

# Paths
currentPath = pathlib.Path(__file__).parent.resolve()
barsPath = f'{currentPath}/src/images/bars/'
containersPath = f'{currentPath}/src/images/containers/'
lootsPath = f'{currentPath}/src/images/loots/'
corpsesPath = f'{currentPath}/src/images/corpses/'
monstersPath = f'{currentPath}/src/images/monsters/'

# Windows
window = 3423, 0, 177, 1080
lootRange = 2434, 353, 239, 246
lootWindow = 3424, 708, 176, 372
battleWindow = 3425, 372, 175, 172
barsWindow = 3430, 145, 150, 35
miniMap = 3431, 31, 114, 112


# Cave waypoints
targetName = 'swamptroll' # swamp troll venore cave to south


# Tests
# newwindow = pyautogui.locateOnScreen("lootrange.png")
# print(newwindow)

# window = pyautogui.screenshot(region=lootWindow)
# window.save('teste1.png')