# Here I'm going to make an automated program which will follow all the followers of a targeted account in Twitter
# Although in the course they're doing this with Instagram, when I try to make an Instagram account, it gets suspended

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

CHROME_DRIVER_PATH = "C:\\chrome-driver\\chromedriver.exe"
TARGETED_ACCOUNT = "Wanindu49"


class TwitterFollower:

    def __init__(self):
        service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = Chrome(service=service)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


follower = TwitterFollower()
follower.login()
follower.find_followers()
follower.follow()