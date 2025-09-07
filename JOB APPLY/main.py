import pyautogui as pg
from time import sleep
import pyperclip
sleep(2)
# print(pg.position())
# exit()
logo = True
a = -200
for i in range(30):
    try:
        sleep(1)
        pg.click(178,22)
        sleep(1)
        pg.click(200,200)
        sleep(1)
        pg.scroll(a)
        sleep(1)
        x,y = pg.locateCenterOnScreen("python.png", confidence=0.8)
        sleep(1)
        pg.click(x,y)
        sleep(1)
        try:
            sleep(1)
            x,y = pg.locateCenterOnScreen("apply01.png", confidence=0.8)
            sleep(1)
            pg.click(x,y)
            sleep(3)
            while logo:
                try:
                    sleep(2)
                    pg.locateCenterOnScreen("naukri.png", confidence=0.8)
                    sleep(1)
                    pg.scroll(-1000)
                    logo = True
                    sleep(1)
                    try:
                        x,y = pg.locateCenterOnScreen("tick.png",confidence=0.8)
                        sleep(1)
                        pg.click(x,y)
                        sleep(1)
                        pg.click(1638,1004)
                        sleep(1)
                    except:
                        pass

                    try:
                        sleep(1)
                        x,y = pg.locateCenterOnScreen("ans.png", confidence=0.5)
                        sleep(1)
                        pg.click(x,y)
                        print(1)
                        pg.click(x,y-65,interval=0.3,clicks=3)
                        pg.hotkey("ctrl","c")
                        que = pyperclip.paste().lower()
                        print(que)

                        file = open("questions.txt","a")
                        file.write(f"{que}\n")
                        file.close()
                        
                        pg.press("tab")
                        sleep(1)

                        if("reason for change from your current company" in que):
                            pg.typewrite("Looking for better growth, new challenges, and opportunities to expand my skills and career.",0.1)
                        
                        if("birth" in que):
                            pg.typewrite("12/09/1997",0.1)

                        if("current company" in que):
                            pg.typewrite("Path Finder",0.1)
                        
                        if("current ctc" in que):
                            pg.typewrite("4.2",0.1)

                        if("expected ctc" in que):
                            pg.typewrite("5.0",0.1)

                
                        
                        if("professional experience" in que):
                            pg.typewrite("2 years",0.1)
                        
                        if("current location" in que):
                            pg.typewrite("nagpur",0.1)

                        if("expect from your next job" in que):
                            pg.typewrite("Challenging projects, skill growth, supportive team, and opportunities to contribute meaningfully.",0.1)
                        
                        if("why should we hire you" in que):
                            pg.typewrite("Skilled in API, backend, and database; quick learner and committed to delivering quality work.",0.1)

                        exp2 = ["javascript","python","jquery","ocr","database","it","django","flask","data structures","docker","bootstrap","postgre","sql","software development","web development","pandas","github","pycharm","Java","C Programming","C++","MySQL","numpy","pandas"]

                        exp1 = ["scikit-learn","matplotlib","react","aws"]
                        for i in exp2:
                            if("experience" in que and i.lower() in que):
                                pg.typewrite("2 years",0.1)
                            
                        for i in exp1:
                            if("experience" in que and i.lower() in que):
                                pg.typewrite("1 year",0.1)

                        sleep(1)
                        pg.press("enter")
                        sleep(2)
                        pg.scroll(1000)
                        sleep(1)

                    except:
                        print("question not found")
                        sleep(1)
                except:
                    print("none")
                    sleep(1)
                    pg.hotkey("ctrl","w")
                    logo = False
                    sleep(1)
                    break
                
        except:
            sleep(1)
            pg.hotkey("ctrl","w")
            sleep(1)
    except:
        pg.scroll(a)
        sleep(1)