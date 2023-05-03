import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
h3 = soup.find(name='h3')
print(h3)