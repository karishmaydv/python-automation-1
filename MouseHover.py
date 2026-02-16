import selenium
from selenium import webdriver
from chromedriver_autoinstaller import install as install_chromedriver
from selenium.webdriver import ActionChains



install_chromedriver()
driver = selenium.webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(60)

#error while using this

#driver = webdriver.Chrome(executable_path="C:\Users\Dell Latitude\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com")

#driver.find_element_by_name("username").send_keys("Admin")

#driver.find_element_by_xpath("//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("Admin")

#driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_xpath("//input[@placeholder='Password']") .send_keys("admin123")

driver.find_element_by_xpath("//button[@type='submit']").click()









