import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    #baseURL = "https://admin-demo.nopcommerce.com/"
    # baseurl ke jagah readproepties me se readconfig clas use krenge
    baseURL = ReadConfig.getApplicationURL()
    #username =  "admin@yourstore.com"
    username = ReadConfig.getUseremail()
    #password = "admin"
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

#test method

    def test_homepageTitle(self,setup):

        self.logger.info(" ********** Test_001_Login ******* ")
        self.logger.info("****** verifying test_homepageTitle ******")
        self.driver =  setup
        #self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()


        time.sleep(2)
        if act_title =="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******  test_homepageTitle  is passed ******")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")

            self.driver.close()
            self.logger.info("******  test_homepageTitle  is failed ******")

            assert False
# this is the actual test cases
        def test_login(self,setup):
            self.driver = setup
            #self.driver = webdriver.Chrome() this is remove by conftest pytest fixture
            self.driver.get(self.baseURL)
            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            act_title = self.driver.title
            self.driver.close()

            if act_title == "Customers / nopCommerce administration":
                assert True
            else:
                assert False
