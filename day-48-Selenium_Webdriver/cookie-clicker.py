# Here I am going to "hack" a clicking game with Selenium

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

chrome_driver = "C:\\chrome-driver\\chromedriver.exe"
URL = "https://orteil.dashnet.org/experiments/cookie/"
service = Service(executable_path=chrome_driver)
driver = Chrome(service=service)

driver.get(URL)

button = driver.find_element(By.ID, "cookie")

# Game loop
while True:
    button.click()
