import time

from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")


#select dropdown -select tag in html element select class will use
#https://rahulshettyacademy.com/angularpractice/

dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("male")
dropdown.select_by_index(0)
dropdown. select_by_value()


