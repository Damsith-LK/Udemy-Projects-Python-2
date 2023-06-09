# Here I am going to make a bot that will tweet my internet speed if it is slower than the speed my internet provider agreed
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import config


CHROME_DRIVER_PATH = "C:\\chrome-driver\\chromedriver.exe"
SPEED_TEST_URL = "https://www.speedtest.net"

class InternetSpeedBot:

    def __init__(self):
        service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = Chrome(service=service)
        self.driver.maximize_window()
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
        """Tweets the internet speeds got from the get_internet_speed() method"""

        # Going to the twitter log in page
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(1)
        # Entering the email
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(config.EMAIL)
        time.sleep(1)
        # Clicking on "Next" button
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        time.sleep(1)

        try:  # Trying to enter the password
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(config.PASSWORD)
        except NoSuchElementException:  # If it asks for username
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(config.USERNAME)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()  # Clicking on "Next Button"
            time.sleep(1)
            # Entering the password
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(config.PASSWORD)
            time.sleep(1)

        # Clicking on "Log In" button
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()


speed_bot = InternetSpeedBot()
speed_bot.tweet_at_provider()
