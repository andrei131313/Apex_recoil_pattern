import pyautogui
import time
import win32api
#import random
import keyboard
import math
import cv2
import numpy as np

horizontal_range = 2
#min_vertical = 3
#max_vertical = 5
min_firerate = 0.03
max_firerate = 0.04
toggle_button = 'caps lock'
enabled = False

# Set the radius of the circle and the starting angle
radius = 10
angle = 0


def is_mouse_down():   #verifica daca mouse ul este apasat
    lmb_state = win32api.GetKeyState(0x01)  #ia state-ul key-ului LMB care are valoarea 0x01 in windowsAPI. RMB are 0x02, ENTER are 0x0D etc.
    return lmb_state < 0  #returns 0 daca LMB este apasat. lmb_state < 0 daca este apasat si lmb_state > 0 daca nu este apasat.

print("Anti-recoil script started!")
if enabled:   #enabled are val initiala 0 (False).
    print("ENABLED")
else:
    print("DISABLED")

last_state = False
vertical_o = 0
while True:
    key_down = keyboard.is_pressed(toggle_button)  #are val True daca tasta toggle_button e apasata.
    for i in range(1,13): #de la 1 la 12 cate taste function sunt. adica F1, F2, F3 etc.
        k = keyboard.is_pressed('f'+str(i)) # verifica ce tasta function e apasata
        if k == True:
            vertical_o = i #vertical_o care controleaza reculu ia val lu i care e nr de la tasta function
            break
    #print(vertical_o)
    if key_down != last_state:  #vedem daca s a schimbat starea lu key_down, adica a fost apasata tasta toggle_down
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("Anti-recoil ENABLED")
            else:
                print("Anti-recoil DISABLED")

    if enabled:  #is_mouse_down() and
        # Calculate the horizontal and vertical offsets
        horizontal_offset = radius * math.cos(angle)
        vertical_offset = radius * math.sin(angle)

        # Simulate a mouse movement by the specified amount
        win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))
        angle += 0.1
        time.sleep(0.001)
    time.sleep(0.001)