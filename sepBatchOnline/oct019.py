# terminal ===> pip install bs4


# from bs4 import BeautifulSoup
# import requests

# url = "https://moviesmod.day/page/2/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# totalPosts = soup.findAll("h2", class_="title front-view-title")

# for i in totalPosts:
#     print(i.text)
#     print()

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩



from bs4 import BeautifulSoup
import requests

url = "https://moviesmod.day/download-jurassic-world-chaos-theory-season-1-2-hindi-english-720p-1080p/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

totalPosts = soup.findAll("div", class_="thecontent clearfix")

print(totalPosts)
# for i in totalPosts:
#     print(i.text)
#     print()