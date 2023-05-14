# Here I am going to make program which checks for job applications on LinkedIn, save them and follow the companies who have posted job applications
# In the course, they recommend to actually apply to jobs, but since I can't do that, this is what I'm going to be doing

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\\chrome-driver\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = Chrome(service=service)
