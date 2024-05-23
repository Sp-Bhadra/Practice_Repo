import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_object = Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
driver = webdriver.Chrome(service=driver_object)
driver.maximize_window()
driver.get("https://www.flipkart.com/")

driver.implicitly_wait(15)
driver.find_element(By.XPATH, "//span[@role='button']").click()
mouse = ActionChains(driver)
mouse.move_to_element(driver.find_element(By.XPATH, "//span[text()='Electronics']")).perform()
mouse.move_to_element(driver.find_element(By.XPATH, "//a[text()='Computer Peripherals']")).perform()
driver.find_element(By.XPATH, "//a[text()='Monitors']").click()
driver.execute_script("window.scroll(0,700)")
# monitors = driver.find_elements(By.XPATH, "//a[@class='_1fQZEK']//div[@class='_4rR01T']")
# for product in monitors:
#     if product.text == "Acer 27 inch Full HD LED Backlit IPS Panel White Colour Monitor (HA270)":
#         product.click()
driver.find_element(By.XPATH, "//div[text()='Acer 27 inch Full HD LED Backlit IPS Panel White Colour Monitor (HA270)']").click()
tabs = driver.window_handles
driver.switch_to.window(tabs[1])
conf = driver.find_element(By.XPATH, "//span[@class='B_NuCI']").text
print(conf)
assert "Acer 27 inch Full HD LED Backlit IPS Panel White Colour Monitor (HA270)" in conf
# driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']").click()
# again_conf = driver.find_element(By.XPATH, "//a[text()='Acer 27 inch Full HD LED Backlit IPS Panel White Colour Monitor (HA270)']").text
# print(again_conf)
# assert "Acer 27 inch Full HD LED Backlit IPS Panel White Colour Monitor (HA270)" in again_conf
driver.get_screenshot_as_file("screen.png")
time.sleep(3)
