# to remove duplication of webdriver in test loin page this file is creted
from selenium import webdriver
import pytest




@pytest.fixture()

def setup():
    driver = webdriver.Chrome()
    return driver