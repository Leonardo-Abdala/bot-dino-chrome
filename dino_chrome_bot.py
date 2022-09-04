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
    
    # If the distance between enemies is less than 400, keep the maximum distance set ex
    if ex < 400:
        max = ex 
    # If not, calculate another 100 pixels ahead to ensure the bot will detect enemies
    else:
        max = ex +100   

    for i in range(ex-100,max):
        enemy_color1 = screen.getpixel((i, ey))
        if enemy_color1 != background_color:
            return True
        # return True for a detected enemy
    
# Dino Jumps
def jump():
    global ex
    pyautogui.press("up")
    if ex < 600: # Maximum distance between dino and enemies
        ex += 3  # Increment in detection region for increase speed of game


print("Start in 5 seconds...")
time.sleep(5.0)


# Infinite Loop of bot
while True:
    screen = capture_screen()
    if detect_enemy(screen):
        jump()
