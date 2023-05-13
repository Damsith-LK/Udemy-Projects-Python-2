# Here I am going to "hack" a clicking game with Selenium

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver = "C:\\chrome-driver\\chromedriver.exe"
URL = "https://orteil.dashnet.org/experiments/cookie/"
service = Service(executable_path=chrome_driver)
driver = Chrome(service=service)

driver.get(URL)

button = driver.find_element(By.ID, "cookie")

upgrades = [
    'buyCursor', 'buyFactory', "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal",
    "buyTime machine"
]

timeout = time.time() + 5  # 5 seconds
five_min = time.time() + 60 * 5  # 5minutes


# Game loop
while True:
    # Clicking
    button.click()
    # check the right-hand pane to see which upgrades are affordable and purchase the most expensive one.
    # You'll need to check how much money (cookies) you have against the price of each upgrade.
    if time.time() > timeout:
        current_money = int(driver.find_element(By.ID, "money").text.replace(",", ""))  # Turning into an int
        prices = [i.text for i in reversed(driver.find_elements(By.CSS_SELECTOR, "#store b"))]
        prices.remove("")
        for upgrade in reversed(upgrades):
            price = int(prices[(upgrades.index(upgrade) + 1) * -1].split("- ")[1].replace(",", ""))  # Turning into an int
            if current_money >= price:
                upgrade_button = driver.find_element(By.XPATH, f'//*[@id="{upgrade}"]/b')
                upgrade_button.click()
                time.sleep(1)
                continue
        timeout += 5
