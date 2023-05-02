# Here I'm scraping an actual live website

from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
content = response.text  # Getting the source code of the page

soup = BeautifulSoup(content, 'html.parser')
articles = soup.find_all(name="span", class_='titleline')

article_texts = [text.a.getText() for text in articles]
article_links = [link.a.get('href') for link in articles]
article_votes = [int(score.getText().split(' ')[0]) for score in soup.find_all(name="span", class_="score")]  # get the votes as an int
print(article_texts)
print(article_links)
print(article_votes)
