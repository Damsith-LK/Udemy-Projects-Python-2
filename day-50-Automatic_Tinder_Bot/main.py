# Here I'm going to make an automatic Tinder Swiping Bot
# I AM NOT DOING THIS CUZ I LIKE THIS, I'M DOING THIS FOR THE COURSE ( ˘︹˘ )

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "C:\\chrome-driver\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = Chrome(service=service)
driver.maximize_window()

URL = "https://tinder.com/"
driver.get(URL)
main_page = driver.current_window_handle

driver.find_element(By.XPATH, "//*[text()='Log in']").click()  # Clicking on "Log In"
# Can't find out a way to automatically click on "Log In with Google", so going to do it manually
time.sleep(5)