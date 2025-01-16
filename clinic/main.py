from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


img = Image.open('clinic.jpg')
def txt(text, x,y, lan):
    global img
    txt = ImageDraw.Draw(img)
    if(lan=="eng"):
        myFont = ImageFont.truetype('bb.otf', 42)
    if(lan=="hin"):
        myFont = ImageFont.truetype('HIMALAYA.TTF', 42)
    txt.text((x, y), text, font = myFont, fill =(255, 0, 0))



txt("Aadesh Lokhande", 390, 925, "eng")
txt("25/M", 850, 925, "eng")
txt("UID : 999999999", 1430, 925,"eng")
txt("18 - 12 - 2023", 2030, 925, "eng")

txt("59 KG",390, 1050, "eng")
txt("Drugs With Intructions",390, 1170, "eng")
txt("MORNING      NOON       NIGHT    TOTAL",1560, 1170, "eng")
txt('  ;"ax     b.]kx/    /.t',1560, 1250, "hin")
txt('  ;s.U+0     b.]kx/   /.t',1560, 1320, "hin")


txt("T PANQUB D Before Meals / khali pet", 390, 1660, "eng")
txt("1                     0                1                6", 1650, 1660, "eng")

txt("T PANQUB D Before Meals / khali pet", 390, 1770, "eng")
txt("1                     0                1                6", 1650, 1770, "eng")

txt("T PANQUB D Before Meals / khali pet", 390, 1890, "eng")
txt("1                     0                1                6", 1650, 1890, "eng")
img.save(f"done.png")








