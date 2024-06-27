import requests
from bs4 import BeautifulSoup


url = f"https://www.gadgets360.com/xiaomi-14-price-in-india-122174"
grab = requests.get(url)
soup = BeautifulSoup(grab.text, 'html.parser')

ModelName= soup.find("div",class_="_thd _shins").text.strip()

# ****************** Key Specs ******************

specs = soup.find('div',class_="_pdswrp").findAll("div",class_="_pdsd")
keySpecs = {}
for i in specs:
    specKey = i.find("span",class_="_ttl").text
    specvalue = i.find("span",class_="_vltxt").text
    keySpecs[specKey] = specvalue

# ****************** fullSpecifications ******************

fullSpecifications = {}
FullSpecs = soup.findAll('div',class_="_gry-bg _spctbl _ovfhide")

for FullSpec in FullSpecs:
    title = FullSpec.find("div",class_="_hd").text
    genRows = FullSpec.findAll("tr")
    try:
        genralSpecifications = {}
        for genRow in genRows:
            genCells = genRow.findAll("td")
            genralSpecifications[genCells[0].text] = genCells[1].text    
    except:
        pass
    fullSpecifications[title] = genralSpecifications

print(fullSpecifications)