#from one window to switch on another window

from selenium.webdriver.common.by import By

from selenium import webdriver




driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(5)
#driver.maximise.window()
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1]) # it will open 1 child windows index
print (driver.find_element(By.TAG_NAME,"h3").text)
# scope is in child windown it will not work will use swith comd
driver.close()
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text