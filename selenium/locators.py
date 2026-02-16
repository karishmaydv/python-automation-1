import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
#Version 134.0.6998.178 (Official Build) (64-bit) latest chrome browser version
# 2 steps to invoke chrome browser

#chrome driver service it is a middleman first it will interact driver version andbrowser verision it goes to internet
#service("chrome driver path ")
#service_obj= Service(r"C:\\Users\\Dell Latitude\\Downloads\\chromedriver_win32.exe")
#driver = webdriver.Chrome(service=service_obj)


driver = webdriver.Chrome()
#driver = webdriver.Firefox() # invoke the firefox url
driver.get("https://rahulshettyacademy.com/angularpractice/")

# locators- id css selector xpath
driver.find_element(By.NAME,"email").send_keys("karishmaknw@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345678")
driver.find_element(By.ID,"exampleCheck1").click()
# for submit button

# xpath format - //tagname[@attribute= 'value']  //input[@type='submit']
#css format - tagname[attribute= 'value']
# # id will turn out to be css selector
# .classname will change in css also
driver.find_element(By.XPATH,"//input[@type='submit']").click()
# for the msg print for submitted succsessfully

# class = alert alert-success alert-dismissible 3 differnet class here
# class= // tagname[attribute= 'value']
message = driver.find_element(By.CLASS_NAME,"alert ").text
print(message)
# name button
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("karishma")
assert "success" in message

time.sleep(2) # it will make script 2 sec wait
