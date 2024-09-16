import pyautogui as pg
import time
import pandas as pd

FailSafeException=True


#OPENING THE TALLY APPLICATION


pg.click(x=2,y=1080,button="left")

time.sleep(1)

pg.write("Tally")


time.sleep(1)

pg.press("enter")

time.sleep(10)

pg.press("f1")

time.sleep(2)


pg.write("devansh")

time.sleep(2)

