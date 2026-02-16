import time

from selenium.webdriver.support.select import Select
name="karishma"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert

alertText = alert.text # it will fetch the alert text
print(alertText)
assert name in alertText
time.sleep(2)
alert.accept() # it will give positive alert like okay yes
#alert.dismiss() # it will give neg alert