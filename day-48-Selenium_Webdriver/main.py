from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\chrome-driver\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.example.com/")
element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)

driver.quit()
