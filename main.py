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

    for i in range(300, 415):
        for j in range(563, 650):
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