import pyautogui as pg
from time import sleep

sleep(2)

file = open("PHP\\Questions.txt","r")
questions = file.readlines()
file.close()

# print(questions)
for que in questions[42:]:
    pg.typewrite(que.replace("\n",""), 0.06)
    sleep(2)
    pg.press("enter")
    sleep(15)
