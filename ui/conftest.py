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
    driver.maximize_window()
    driver.get(Settings.baseurl + 'clear')
    driver.get(Settings.baseurl + 'login')
    functions.findec(driver, Locator.InputLogin, Settings.login)
    functions.findec(driver, Locator.inputPassword, Settings.password)
    functions.findec(driver, Locator.buttonIn, "PressElement")
    yield driver
    driver.quit()