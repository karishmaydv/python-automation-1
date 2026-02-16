import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from chromedriver_autoinstaller import install as install_chromedriver

install_chromedriver()
driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(60)


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#copytest buttton to double click
element = driver.find_element("xpath","//*[@id=HTML10]/div[1]/button]")
actions = ActionChains(driver)
actions.double_click(element).perform() #doubleclick on button

