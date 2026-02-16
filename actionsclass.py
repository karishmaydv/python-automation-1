# action class is used to
#hover or move element right click double click and drag and drop



import time

import driver

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

driver.implicitly_wait(5)
driver.maximize.window()

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.double_click(driver.find_element(By))
#action.context_click(driver.find_element(By)) # right click of element
#action.drag_and_drop()
# perform text need to add to perform and mousehove means moving element
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform() # click on mouse hover
action.context_click(driver.find_element(By.PARTIAL_LINK_TEXT,"Top")).perform() # right click the mouse and select top
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()