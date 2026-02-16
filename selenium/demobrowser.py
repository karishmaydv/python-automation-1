import time
from selenium import webdriver
from selenium.webdriver.ie.service import Service
#Version 134.0.6998.178 (Official Build) (64-bit) latest chrome browser version
# 2 steps to invoke chrome browser

#chrome driver service it is a middleman first it will interact driver version andbrowser verision it goes to internet
#service("chrome driver path ")
#service_obj= Service(r"C:\\Users\\Dell Latitude\\Downloads\\chromedriver_win32.exe")
#driver = webdriver.Chrome(service=service_obj)


#driver = webdriver.Chrome()
driver = webdriver.Firefox() # invoke the firefox url
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print (driver.current_url)









time.sleep(2) # it will make script 2 sec wait