import requests
from bs4 import BeautifulSoup


url = f"https://www.gadgets360.com/mobiles/acer-phones"
grab = requests.get(url)
soup = BeautifulSoup(grab.text, 'html.parser')

modelsDict = {}
AllModels= soup.findAll("a",class_="rvw-title")
for model in AllModels:
    name = model.text 
    url = model["href"]
    modelsDict[name] = url 

file = open("StoreDataModel.py","a")
file.write(f"{modelsDict}\n")
file.close()


# ===================================================
