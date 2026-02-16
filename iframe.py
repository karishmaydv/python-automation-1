# iframe is separed entity and embeded to html websites
#from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
# below cmd used to open iframe

driver.switch_to.frame("mce_0_ifr") # frame id
driver.find_element(By.ID,"tinymce").clear() # it is giving error 
time.sleep(2)
driver.find_element(By.ID,"tinymce").send_keys("Iam able to automate frames")
# if you will run program getting error no such element becoze this is not a browser scope its in iframe


'''another 
method'''
'''
iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)
editor = driver.find_element(By.ID, "tinymce")
editor.clear()  # May not work properly here – see next step
driver.find_element(By.ID,"tinymce").send_keys("Iam able to automate frames")
'''

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)







