# https://thejujutsukaisenread.com/jujutsu-kaisen-chapter-1/

import pyautogui as pg
from time import sleep


sleep(2)
for i in range(200):
    try:
        x,y = pg.locateCenterOnScreen("down.png", confidence=0.8)
        pg.click(x,y)
        sleep(1)
    except:
        pg.scroll(-400)