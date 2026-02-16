import time

from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind") # it will select only 1 particular countires
time.sleep(2)

#it will give all courntires list from the dropdown
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))  # len with list variables

for country in countries:
    if country.text == "India":
        country.click()
        break

#print(driver.find_element(By.ID, "autosuggest").text) # this will not give text for dynamic value
# another method will use for this

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"