import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import Settings, Locator
from selenium.webdriver.support import expected_conditions as EC
import functions
@pytest.fixture()
def driver(request):
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome('/chromedriver', chrome_options=options)
    try:
        driver.get(Settings.baseurl + 'login')
        element = functions.findec(driver, Locator.InputLogin)
        element.send_keys(Settings.login)
        element = functions.findec(driver, Locator.inputPassword)
        element.send_keys(Settings.password)
        element = functions.findec(driver, Locator.buttonIn)
        element.click()
    except:
        driver.get(Settings.baseurl)
    yield driver
    driver.quit()