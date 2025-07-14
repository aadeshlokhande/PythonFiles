from bs4 import BeautifulSoup

filee = open("scrapData.txt","w", encoding="utf-8")
with open('data.txt', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')


    # Example 1: Extract plain text messages
    messages = soup.find_all('div', class_='copyable-text')
    for msg in messages:
        text = msg.get_text(strip=True)
        print("Message:", text)
        print(text,file=filee)
filee.close()
    #
    # Example 2: Extract timestamp
    # timestamps = soup.find_all('span', class_='x1rg5ohu')
    # for time in timestamps:
    #     print("Time:", time.text.strip())

    # Example 3: Extract all emojis
    # emojis = soup.find_all('img', class_='emoji')
    # for emoji in emojis:
    #     alt = emoji.get('alt')
    #     print("Emoji:", alt)
