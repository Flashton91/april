import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import Settings, Locator
from selenium.webdriver.support import expected_conditions as EC

def findec(driver, locator, action):
    timeout = 15
    element_present = EC.element_to_be_clickable((By.XPATH, locator))
    element = WebDriverWait(driver, timeout).until(element_present)
    if action == "PressElement":
        element.click()
        return driver
    if action == "TakeElement":
        return driver
    else:
        element.send_keys(action)
        return driver

def roleSelectGVI(driver):
    try:
        findec(driver, Locator.buttonGVI, "PressElement")
    except:
        driver.get(Settings.baseurl)
        driver.refresh()
        findec(driver, Locator.buttonGVI, "PressElement")
        driver.refresh()
    return driver

def scrollDown(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return driver

def generateUserDataRnd(driver):
    