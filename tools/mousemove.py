import sys
import time
import pyautogui
import cv2
import numpy as np
#pip install opencv-contrib-python
#pip install pyautogui

#https://github.com/asweigart/pyautogui
current = pyautogui.position()
cx = sx = current[0]
cy = sy = current[1]

mx = 20
my = 20
vx = vy = 30

print("Moving", mx, my, "with", vx, "pixels per second")
print("Press 'q' to quit")


last = time.time()
x=500
while (True):
    c = cv2.waitKey(1)
    if c == 27:  # Esc quit if c == ord('Q'):
        sys.exit()

    current = time.time()
    tick = current - last
    last = current
    x=x+50
    y=np.sqrt(1000000-x^2)
    y=1100
    if x>1000:
        x=500
    pyautogui.moveTo(x,y)
    print(x,y)
    pyautogui.click(button='right')
    time.sleep(6.001)
