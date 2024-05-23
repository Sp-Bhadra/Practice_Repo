import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
#driver.minimize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
# driver.find_element(By.ID,"name").send_keys("Chinmaya")
# driver.find_element(By.NAME, "enter-name").send_keys("Chinmaya")
#driver.find_element(By.CLASS_NAME,"inputs").send_keys("Chinmaya")
driver.find_element(By.TAG_NAME,"input").send_keys("Chinmaya")
time.sleep(5)
# driver.get("https://google.com")
# driver.forward()
# driver.back()
driver.refresh()
driver.close()