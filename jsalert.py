import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.find_element(By.NAME,"alert").click()
alert = driver.switch_to.alert
alertext = alert.text
print(alertext)
time.sleep(2)
alert.accept()
time.sleep(5)