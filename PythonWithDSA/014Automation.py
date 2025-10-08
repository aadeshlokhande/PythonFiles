# ████████████████████ Automation ████████████████████

# web
# desktop
# terminal cmd
# ████████████████████ pyautogui ████████████████████

# ctrl + r -----> run 
# cmd ---> enter 

# >>> pip install pyautogui ---> windows
# >>> pip3 install pyautogui ---> linux, mac

# import pyautogui as pg 
# from time import sleep
# sleep(3)
# keyboard 
# press 
# pg.press("win")

# type 
# pg.typewrite("mera name aadesh hai.... mai ek acha bacha hu", 0.09)

# shortcuts (ctrl+c)
# pg.hotkey("ctrl", "a")


# mouse
# position
# a = pg.position()
# print(a)

# click 
# pg.click()
# pg.click(100,100,clicks=100,interval=1)

# double click 
# pg.doubleClick()
# pg.doubleClick(200,200)

# right click
# pg.rightClick()
# pg.rightClick(200,200)

# move 
# pg.move(400,200,3)
# pg.moveTo(400,200,3)

# drag 
# pg.drag(400,300,1)
# pg.dragTo(400,300,1)

# scroll
# pg.scroll(400)


# a,b = pg.locateCenterOnScreen("like.png")
# pg.click(a,b)

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# import pyautogui as pg 
# from time import sleep
# sleep(3)

# pg.press("prtsc")
# sleep(1)
# pg.moveTo(10,10,3)
# pg.dragTo(400,500,3)

# pg.moveTo(957,985,1)
# pg.click()

# No = 7058232826
# url = f"wa.me/91{No}?text="
# msg = "Hello bhai\nkaise ho".replace(" ", "%20").replace("\n","%0A")
# finalurl = url+msg

# import pyautogui as pg
# from time import sleep

# sleep(3*45*60)
# msg = "I love you baby... :-* :-) "
# for i in range(10):
#     pg.typewrite(msg, 0.1)
#     pg.press("enter")

# appname = input("enter app name = ")
# sleep(1)
# pg.press("win")
# sleep(1)
# pg.typewrite(appname,0.1)
# sleep(1)
# pg.press("enter")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

# import pyautogui as pg
# from time import sleep

# sleep(2)

# url = "https://www.instagram.com/aadesh.py/"
# cmd = input("enter a cmd = ")

# if("khul ja sim sim" == cmd):
#     pg.press("win")
#     sleep(1)
#     pg.typewrite("brave",0.1)
#     sleep(1)
#     pg.press("enter")
#     sleep(5)
#     pg.hotkey("win", "up")                  # full screen
#     sleep(1)
#     # pg.hotkey("ctrl", "e")                  # search bar
#     # sleep(1)
#     pg.typewrite(url,0.1)
#     pg.press("enter")
# else:
#     print("cmd galat hai")

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
# solution.txt
# my name is aadesh ..... 

# main.py
# data = my name is aadesh ..... 
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
