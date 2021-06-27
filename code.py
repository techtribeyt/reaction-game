import keyboard
import pyautogui
import numpy as np
import cv2
import time
import sys

# button to press to start the program
start_button = "p"

def analyze_image(img):
    lower_col = (65, 60, 240)
    upper_col = (75, 70, 250)
    mask = cv2.inRange(img, lower_col, upper_col)
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    if contours and cv2.contourArea(contours[0]) > 100000:
        pyautogui.press(start_button)
        sys.exit()
        
while True:
    # start the program
    if keyboard.is_pressed(start_button):
        break
    
time.sleep(2)
while True:
    # take screenshot and analyze
    scrot = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
    analyze_image(scrot)