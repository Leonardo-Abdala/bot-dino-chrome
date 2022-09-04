#!/usr/bin/python

# Leonardo Abdala

import time

from PIL import ImageGrab
import pyautogui

# Use the position to take the ponts of dino and the enemies
# print(pyautogui.position())

# Dino position
dx = 105 
dy = 436
# Enemy position
ex = 300
ey = 460
# Background position
bx = 266
by = 121

# Take screenshot using PIL lib
def capture_screen():
    screen = ImageGrab.grab()
    return screen

# Detects enemy by diff in pixel color in region of detections
def detect_enemy(screen):
    background_color = screen.getpixel((bx, by))
    
    # enemy_color2 = screen.getpixel((ex + 10, ey))
    # enemy_color3 = screen.getpixel((ex + 15, ey))
    # enemy_color4 = screen.getpixel((ex + 20, ey))
    # enemy_color5 = screen.getpixel((ex + 25, ey))

    if ex < 400:
        max = ex 
    else:
        max = ex +100   

    for i in range(ex-100,max):
        enemy_color1 = screen.getpixel((i, ey))
        if enemy_color1 != background_color:
            return True
        # if enemy_color3 != background_color or enemy_color2 != background_color or enemy_color1 != background_color or enemy_color4 != background_color or enemy_color5 != background_color:
        #     return True # Return True for a detected enemy
    
# Dino Jumps
def jump():
    global ex
    pyautogui.press("up")
    print("Jump!")
    if ex < 600 :
        ex += 3  # Increment in detection region for increase speed of game


print("Start in 5 seconds...")
time.sleep(5.0)


# Infinite Loop of bot
while True:
    screen = capture_screen()
    print(screen.getpixel((ex, ey)))
    print(screen.getpixel((ex + 10, ey)))
    print(screen.getpixel((ex + 20, ey)))
    print(screen.getpixel((ex + 30, ey)))
    print(screen.getpixel((ex + 40, ey)))
    print("----------------------------")
    if detect_enemy(screen):
        jump()

print("Ex:" + ex)
