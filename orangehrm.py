import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# 
# service_obj = Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://opensource-demo.orangehrmlive.com")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.CSS_SELECTOR,"button.oxd-button").click()
# time.sleep(10)
# driver.find_element(By.CSS_SELECTOR,"span[class = 'oxd-text oxd-text--span oxd-main-menu-item--name']").click()
# time.sleep(10)

service_obj=Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
radioB = driver.find_elements(By.XPATH, "//input[@name='inlineRadioOptions']")
radioB[1].click()
assert radioB[1].is_selected()
time.sleep(3)
time.sleep(3)