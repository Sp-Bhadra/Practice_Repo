# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.execute_script("window.scroll(0,900)")
# action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# time.sleep(5)
# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
# time.sleep(5)
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

deriver_obj = Service("/Users/sprasad/Selenium_Project/Ide_path/chromedriver")
driver = webdriver.Chrome(service=deriver_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radio = driver.find_elements(By.CSS_SELECTOR, "input[name='radioButton']")
for i in radio:
    if i.get_attribute("value")=="radio2":
        i.click()
        assert i.is_selected()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type to Select Countries']").send_keys("ha")
Wait = WebDriverWait(driver,10)
Wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "li[class='ui-menu-item']")))
country = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
for i in country:
    if i.text == "Bahamas":
        i.click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "select[name='dropdown-class-example']")
drop_obj=Select(driver.find_element(By.CSS_SELECTOR, "select[name='dropdown-class-example']"))
drop_obj.select_by_visible_text("Option2")
checkbox = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for k in checkbox:
    if k.get_attribute("value")=="option2":
        k.click()
        assert k.is_selected()
driver.find_element(By.CSS_SELECTOR, "input[value='Alert']").click()
alert = driver.switch_to.alert
text = alert.text
time.sleep(3)
alert.accept()
driver.execute_script("window.scroll(0,999)")
time.sleep(4)
driver.close()