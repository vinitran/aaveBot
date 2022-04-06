import pyautogui
import time
from ctypes import windll
import threading 

import keyboard
def press(button):
    keyboard.press(button)
def isRunning(running):
    running = True
    if (keyboard.is_pressed('SPACE')):
        running = False 
    return running
def moveTo(playerX, playerY, stoneX, stoneY):
    if (playerX < stoneX - 10):
        press('d')
    elif (playerY > stoneY + 10):
        press('a')
    else:
        if (playerY < stoneY - 10):
            press('w')
        elif (playerY > stoneY + 10):
            press('s')
if __name__ == "__main__":
    print("Running in 3 seconds, minimize this windows. To stop the program drag the mouse to the top-left corner of your screen.")
    time.sleep(3)
    running = True
    width, height= pyautogui.size()
    while running:
        running = isRunning(running)
        start = time.time()
        try:
            playerX, playerY = pyautogui.locateCenterOnScreen('player.png',confidence=0.6)
        except:
            try:
                playerX, playerY = pyautogui.locateCenterOnScreen('moveLeftPlayer.png',confidence=0.6)
            except:
                try: 
                    playerX, playerY = pyautogui.locateCenterOnScreen('moveRightPlayer.png',confidence=0.6)
                except:
                    try: 
                        playerX, playerY = pyautogui.locateCenterOnScreen('moveUpPlayer.png',confidence=0.6)
                    except:
                        print("dont detect!")
                        playerX = 600 # random X,Y
                        playerY = 5
        try: #nếu phát hiện được stone thì nó chạy đến, còn k thì tự di chuyển
            try:
                stoneX, stoneY = pyautogui.locateCenterOnScreen('alphaStone.png',confidence=0.75)
            except:
                stoneX, stoneY = pyautogui.locateCenterOnScreen('fudStone.png',confidence=0.75)
            print('detect')
            moveTo(playerX, playerY, stoneX, stoneY)
        except: # tự di chuyển
            # moveTo(playerX, playerY, playerX - 100,playerY) #teast xem nó có đến được vị trí 300x300 trên màn hình k, cho đến góc game để test
            print(time.time()- start)
            button = 'a'
            if playerX < 300:
                button = 'd'
            if playerX > 1200:
                button = 'a'
            press(button)
        

# class Aavegochi():
#     __author__ = "EnriqueMoran"

#     def __init__(self, playX, playY, stoneX, stoneY, x, y):
#         self.playX = playX
#         self.playY = playY
#         self.stoneX = stoneX
#         self.stoneY = stoneY
#         self.movement = 'a'   # đi sang trái đầu
#     def move(self):
#         speed = 0.14
#         if self.movement_buffer[0] == "left" and len(self.movement_buffer) == 2:
#             pyautogui.typewrite(['left', 'left'], speed)
#         elif self.movement_buffer[0]  == "right" and len(self.movement_buffer) == 2:
#             pyautogui.typewrite(['right', 'right'], speed)
#         self.movement_buffer = self.movement_buffer[1:]
#     def get_color(self, rgb):
#         r = rgb & 0xff
#         g = (rgb >> 8) & 0xff
#         b = (rgb >> 16) & 0xff
#         return r,g,b
#     def get_pixel(self, x, y):    # Modify class atribute
#         screen = windll.user32.GetDC(0)
#         rgb = windll.gdi32.GetPixel(screen, x, y)
#         return self.get_color(rgb)

#     def play(self):
#         while True:
#             pixel_color = self.get_pixel(self.x, self.y)
#             if pixel_color == (161, 116, 56):
#                 self.movement_buffer.append("right")
#                 self.move()
#             elif pixel_color == (211, 247, 255) or pixel_color == (241, 252, 255):
#                 self.movement_buffer.append("left")
#                 self.move()
#     x, y = pyautogui.locateCenterOnScreen('branch.png',confidence=0.9)
#     pyautogui.moveTo(x, y + 5)
#     treeX, treeY = playX - 6, playY - 177 # Tree position
#     time.sleep(0.3)
#     print("Im playing... To stop me click on IDLE and press CTRL+F6.")
#     lumberjack = lumberjackBot(playX, playY, treeX, treeY, x, y)
#     lumberjack.play()   # Game start


        
        
        

