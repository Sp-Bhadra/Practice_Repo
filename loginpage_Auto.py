# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com/loginpagePractise")
# driver.implicitly_wait(10)
# username = driver.find_element(By.XPATH,"//i[.='rahulshettyacademy']").text
# password = driver.find_element(By.XPATH,"//i[.='learning']").text
#
# driver.find_element(By.ID,"username").send_keys(username)
# driver.find_element(By.ID,"password").send_keys(password)
# checkbox = driver.find_elements(By.XPATH,"//input[@id='usertype']")
# # RadioButton[1].click()
# # time.sleep(5)
# for check in checkbox:
#     if check.get_attribute("value") == "user":
#         check.click()
#     assert check.is_selected()
# alert = driver.switch_to.alert
# alerttext = alert.text
# print(alerttext)
# time.sleep(5)



import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver_obj = Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
driver = webdriver.Chrome(service=driver_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("kanda")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("kanda@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Kanda@123")
checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for j in checkbox:
    if j.get_attribute("id") == "exampleCheck1":
        j.click()
        assert j.is_selected()
# dropdown = Select(driver.find_elements(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
# dropdown.select_by_visible_text("Female")
dropdown_select=Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
dropdown_select.select_by_visible_text("Female")
redio = driver.find_elements(By.XPATH, "//input[@name='inlineRadioOptions']")
for i in redio:
    if i.get_attribute("id") == "inlineRadio2":
        i.click()
        assert i.is_selected()
driver.execute_script("window.scroll(0,document.body.scrollHeight)")
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)

time.sleep(3)