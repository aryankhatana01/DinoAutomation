import pyautogui
from PIL import Image, ImageGrab 
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def whenhitting(data):
    
    for i in range(300, 370):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(300, 415):  # These are coordinates of the Rectangle in the +ve(x) axis direction
        for j in range(563, 650):  # These are coordinates of the Rectangle in the (-ve)y axis direction
        
        '''First pixel is colored black at (300,563) coordinate, 2nd pixel at (300,564) coordinate and so on
           after that (301,563) then (301,564) and so on last pixel is colored at (415,650)'''
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Focus on the Chrome Dino game window")
    print('Running...')
    time.sleep(3)
     

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        whenhitting(data)

# image = ImageGrab.grab()
# data = image.load()
# for i in range(300, 370):
#     for j in range(563, 650):
#         data[i, j] = 0

# image.show()
