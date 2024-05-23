import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
# time.sleep(3)
# results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
# count = len(results)
# print(count)
# for result in results:
#     result.find_element(By.XPATH,"div/button").click()
driver.find_element(By.ID,"openwindow").click()
windowsopend = driver.window_handles
driver.switch_to.window(windowsopend[1])
time.sleep(4)
