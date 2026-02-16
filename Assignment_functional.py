import time

from numpy.ma.core import append
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
expectedList = ['cucumber ','Raspberry' 'strawberry']
actualList = []


driver = webdriver.Chrome()
driver.implicitly_wait(5)
# 5 sec is max if got result in 2 sec it will proceed further and save time
# if object is not identify it will wait and it apply on whole code.
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# finding css selector by classname
# .classvalue user for id #id value
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
# want to add 2 elements in cart and check so will write xpath from parent to child
#  2div is there
results= driver.find_elements(By.XPATH,"//div[@class='products']/div")
# it will give list of webelements but implicit wait will not work here
count = len(results) # it will count the product
assert count>0
# chaining of webelements

for result in  results :
    # loop interate 2 time click button 2 times

    actualList.append(result.find_element(By.XPATH,"h4").text) # full and beign xpath is in line 27
    # append method is used to update the list
    result.find_element(By.XPATH,"div/button").click() # 3 items added in the cart in via loop
    assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR,"img[alt='cart']").click()