import time

from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# for multiple checkbox this is used and after that list configure and loop to interate another checkbox
checkboxes = driver.find_elements(By.XPATH,"//input[type='checkbox']")
print(len(checkboxes))
# checkbox positon is changing thatswhy using for loop

for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":
        checkbox.click()
        assert checkbox.is_selected() # if it is true test will fail and assertion error give on console
        break

      #  https: // rahulshettyacademy.com / AutomationPractice /
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
# NO NEED TO USE FOR LOOP AS RADIO BUTTONS IS FIXED psotion not changed
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

#displaybox
assert  driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()

