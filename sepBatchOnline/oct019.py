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



# from bs4 import BeautifulSoup
# import requests

# url = "https://moviesmod.day/download-naruto-shippuden-season-1-6-hindi-480p-720p-1080p/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# totalPosts = soup.findAll("div", class_="thecontent clearfix")

# # print(totalPosts)
# for i in totalPosts:
#     print(i.text)
#     print()


# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
url = "https://wallpapercave.com/search?q=makima"
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, "html.parser")
links = soup.findAll("a")

print(soup)

# print(links)
# for link in links:
#      print(link["href"])
#      print()


