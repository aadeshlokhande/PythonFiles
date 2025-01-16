import requests 
from bs4 import BeautifulSoup

file = open("01movieLink.txt","r")


for i in range(14479):
    url = file.readline().replace("\n","")
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        dicData = {}

        # ****************** heading ******************

        heading = soup.find("h1", class_="title single-title entry-title").text
        dicData["Heading"] = heading

        # ****************** movie info ******************
        info = soup.find("div", class_="thecontent clearfix")
        a = info.findAll("li")

        for i in a:
            data = i.text.replace("\xa0",u" ").split(": ")
            dicData[data[0].strip()] = data[1].strip()

        # ****************** storyline ******************
        content = soup.find("div",class_="thecontent clearfix")
        storyline = content.findAll("p")[3].text
        dicData["Storyline"] = storyline.strip()

        # print(dicData)

        file1 = open("002MovieInfo.txt","a")
        file1.write(f"[<>]{dicData["Full Name"].strip()} : {dicData}<[]>,\n")
        file1.close()
    except:
        file1 = open("002MovieError.txt","a")
        file1.write(f"{url}\n")
        print(i,url)
        file1.close()
file.close()