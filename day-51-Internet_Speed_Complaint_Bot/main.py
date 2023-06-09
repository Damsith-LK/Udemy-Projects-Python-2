# Here I am going to make a bot that will tweet my internet speed if it is slower than the speed my internet provider agreed
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import config


CHROME_DRIVER_PATH = "C:\\chrome-driver\\chromedriver.exe"
SPEED_TEST_URL = "https://www.speedtest.net"

class InternetSpeedBot:

    def __init__(self):
        service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = Chrome(service=service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """Fetches the internet speeds from "https://www.speedtest.net" """
        self.driver.get(SPEED_TEST_URL)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()  # Clicking on "Go" button
        time.sleep(50)  # Waiting for it to get the internet speed
        # Getting the download speed
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Download Speed: {self.down}")
        print(f"Upload Speed: {self.up}")

    def tweet_at_provider(self):
        pass


speed_bot = InternetSpeedBot()
speed_bot.get_internet_speed()
