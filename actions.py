import pyautogui

class Actions:
    def __init__(self):
        pass
    
    # Move to minimap x y coordinates
    def move(self, imagem_position):
        x, y = pyautogui.center(imagem_position)
        pyautogui.moveTo(x, y, 0.1)

    # Move and click to minimap x y coordinates
    def move_and_click(self, imagem_position):
        self.move(imagem_position)
        pyautogui.click()

    