# this is the working iframe script

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")

# Switch to iframe
driver.switch_to.frame("mce_0_ifr")

# Locate the content-editable body and clear it using send_keys
editor = driver.find_element(By.ID, "tinymce")
#This simulates pressing Ctrl + A, which is the "Select All" shortcut.
#It selects all the text currently inside the editable element (editor).
editor.send_keys(Keys.CONTROL + "a")
# it will delete all text from editor
editor.send_keys(Keys.BACKSPACE)
#print (editor.send_keys("I am able to automate frames").text) it will give error below mtd will use
text = "I am able to automate frames"
editor.send_keys(text)
print("Typed into iframe:", text)


# Switch back to main document
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text) # it will give text an iframe contain
