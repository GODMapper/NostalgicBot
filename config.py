import pathlib


window = 3423, 0, 177, 1080

currentPath = pathlib.Path(__file__).parent.resolve()

monstersPath = f'{currentPath}/src/images/monsters/'

#TODO move to configs
# Paths
barsPath = f'{currentPath}/src/images/bars/'
containersPath = f'{currentPath}/src/images/containers/'
lootsPath = f'{currentPath}/src/images/loots/'

#TODO move to configs and 
# Coordinates
#left, top, width, height
gameWindow = 1680, 0, 1920, 1080
# TODO Battle window need to be resized to minimum size
battleWindow = 3425, 372, 175, 172
barsWindow = 3430, 145, 150, 35
backpackWindow = 3425, 542, 175, 215

targetName = 'swamptroll' # swamp troll venore cave to south