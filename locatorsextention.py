import time

from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

#service_obj= Service(r"C:\\Users\\Dell Latitude\\Downloads\\chromedriver_win32.exe")
#driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click() #if html tag have a anchor tag it will linktext

# will click on forgot password email and new password html
# fromp parent and child elemenet inxpath
#form/div[1] xpath css form div  when no attribute is there in html
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("karishmaknw@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("12345678")
#driver.find_element(By.XPATH,"//button[@type='submit']").click() t
# basedupon text we can generate xpath also button can
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()



time.sleep(2) # it will make script 2 sec wait