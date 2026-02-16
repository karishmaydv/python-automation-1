import driver
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_options= webdriver.ChromeOptions() # use for headless mode
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors") # it will ignore ssl and connection realted screen page
