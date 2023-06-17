# This project is a capstone project for testing all of my web scraping skills including Selenium and BeautifulSoup
# I think using OOP would be a better approach for this project

from bs4 import BeautifulSoup
import requests
import config


class RentingResearch:

    def __init__(self):
        self.RENTING_WEBSITE_LINK = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.048563375%2C%22east%22%3A-121.96915663671875%2C%22south%22%3A37.39423627832906%2C%22north%22%3A38.02328490484952%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
        self.WEBSITE_URL = "https://www.zillow.com"

    def get_houses_info(self):
        """Fetches relevant information about rent houses from zillow.com using BeautifulSoup
        Returns fetches items in lists"""

        headers = {
            "User-Agent": config.user_agent,
            "Accept-Language": config.accept_language
        }
        response = requests.get(self.RENTING_WEBSITE_LINK, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        houses_ul = soup.find(id="grid-search-results").find(name="ul")
        elements = houses_ul.find_all(name="a", attrs={"class": "property-card-link", "tabindex": "0"}, recursive=True)
        links, prices, addresses = [], [], []

        for element in elements:
            link = element["href"]  # Link to the renting house
            # If there is something wrong with the link (if no https://zillow.com)
            if self.WEBSITE_URL not in link:
                link = self.WEBSITE_URL + link
            address = element.text  # Address of the house
            # Price of the house
            price = element.findAllNext(name="div")[2].findNext(name="span").text.split()[0].replace("+", '').replace("/mo", '')
            # Appending the collected information to corresponding lists
            links.append(link)
            prices.append(price)
            addresses.append(address)

        return links, prices, addresses

    def update(self):
        """Enters the collected data into a Google form using Selenium"""
        pass


rr = RentingResearch()
rr.get_houses_info()
rr.update()