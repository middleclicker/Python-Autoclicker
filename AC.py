import win32api
import win32con
import time
import random
import pyglet
from pynput.mouse import Button, Controller
mouse = Controller()

sound_1 = pyglet.resource.media("ClickOne.mp3", streaming=False)
sound_2 = pyglet.resource.media("ClickTwo.mp3", streaming=False)
sound_3 = pyglet.resource.media("ClickThree.mp3", streaming=False)
def ac():
    if keystate < 0:
        mouse.click(Button.left, 1)
        soundToPlay = random.randint(1, 5)
        if soundToPlay == 1:
            sound_1.play()
        elif soundToPlay == 2:
            sound_1.play()
        elif soundToPlay == 3:
            sound_1.play()
        elif soundToPlay == 4:
            sound_1.play()
        elif soundToPlay == 5:
            sound_2.play()
        else:
            sound_3.play()
        sleeptime = random.randint(6, 11)*0.01
        time.sleep(sleeptime)
    else:
        pass

while True:
    keystate = win32api.GetAsyncKeyState(0x06)
    ac()
