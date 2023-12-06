from bs4 import BeautifulSoup
import requests

song_date = input("Which year you want to select YYY-MM-DD:\n")
url = f"https://www.billboard.com/charts/hot-100/{song_date}/"
response = requests.get(url)
link = response.text
soup= BeautifulSoup(link,"html.parser")

top_100songs = soup.select(selector="li h3")
song_names = [song.getText().strip() for song in top_100songs]
print(song_names)

