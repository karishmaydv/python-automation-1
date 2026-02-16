import selenium
from selenium.webdriver import Chrome
from chromedriver_autoinstaller import install as install_chromedriver
from selenium.webdriver import ActionChains

install_chromedriver()
driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(60)


driver.get("https://opensource-demo.orangehrmlive.com")


# this is the corrct way to write  find element to xpath the error no error onthis
driver.find_element("xpath", "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element("xpath", "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element("xpath", "//button[@type='submit']").click()


admin= driver.find_element("xpath", "//input[@placeholder='Username']")
usermgt =driver.find_element("xpath", "//span[normalize-space()='User Management']")
users = driver.find_element("xpath",  "//a[@role='menuitem']")

actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element("usermgt").move_to_element(users).click().perform()
# this is the method used to mouse hover action when we are hover the mouse from this admin, usermgt, and users