# it is used to scroll down the page in selenium
# headless mode u will not seee browser invocation but from BE it will run
import time

import driver
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_options= webdriver.ChromeOptions() # use for headless mode
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors") # it will ignore ssl and connection realted screen page

# Initialize the driv"er correctly otherwise give error
driver= webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# below cmd use to scroll down the page using javascript

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

driver.get_screenshot_as_file("screen.png") #this is use to take a screenshots and stored
