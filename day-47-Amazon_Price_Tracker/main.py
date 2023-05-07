# The product I am going to track in this project is a PS5

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91/ref=sr_1_2?crid=3OJOOBDL3OVVH&keywords=ps5&qid=1683460711&sprefix=ps%2Caps%2C296&sr=8-2&th=1"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"
}
response = requests.get(url=URL, headers=headers)
contents = response.text
soup = BeautifulSoup(contents, 'html.parser')
print(soup)