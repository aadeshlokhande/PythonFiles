import requests 
from bs4 import BeautifulSoup


for num in range(1,725):
    if(num==1):
        url="https://moviesmod.info/"
    else:
        url = f"https://moviesmod.info/page/{num}/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.findAll("h2", class_="title front-view-title" )
    for i in box:
        a = i.find("a")
        file = open("01movieLink.txt","a")
        file.write(f"{a['href']}\n")
        file.close()
        print(f"page : {num} ----> {a.text}")

