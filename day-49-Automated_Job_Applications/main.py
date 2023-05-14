# Here I am going to make a program which checks for job applications on LinkedIn, save them and follow the companies who have posted job applications
# In the course, they recommend to actually apply to jobs, but since I can't do that, this is what I'm going to be doing

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import config

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3600710880&f_AL=true&f_WT=2&geoId=100446352&keywords=python%20developer&location=Sri%20Lanka&refresh=true"
chrome_driver_path = "C:\\chrome-driver\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = Chrome(service=service)

driver.get("https://www.linkedin.com")

driver.find_element(By.ID, "session_key").send_keys(config.email)  # Entering the e-mail
driver.find_element(By.ID, "session_password").send_keys(config.password)  # Entering the password
driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()  # Clicking on sign-in button
# driver.find_element(By.XPATH, '//*[@id="ember459"]/button').click() In case of phone number verification

time.sleep(13)
