# Here I'm scraping an actual live website

from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
content = response.text  # Getting the source code of the page

soup = BeautifulSoup(content, 'html.parser')
article_tag = soup.find(name="span", class_='titleline')
article_text = article_tag.a.getText()
article_link = article_tag.a.get('href')
article_votes = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_votes)