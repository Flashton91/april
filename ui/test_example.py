import time

import functions
from data import Settings, Locator
from selenium import webdriver

def test_ex(driver):
    driver.implicitly_wait(Settings.standarttime)
    driver.get(Settings.baseurl)
    element = functions.findec(driver, Locator.buttonGVI)
    element.click()
    driver.implicitly_wait(Settings.standarttime)
    driver.get(Settings.baseurl + "medical-studies")
    driver.implicitly_wait(Settings.standarttime)
    element = functions.findec(driver, Locator.buttonAdd)
    element.click()
    driver.implicitly_wait(Settings.standarttime)
    element = functions.findec(driver, Locator.inputPsurname)
    element.send_keys("ВместоИмя")
    element = functions.findec(driver, Locator.inputPname)
    element.send_keys("ВместоФамилии")
    element = functions.findec(driver, Locator.buttonSearch)
    element.click()
    driver.implicitly_wait(Settings.standarttime)
    functions.scrollDown(driver)
    driver.implicitly_wait(Settings.standarttime+30)
    element = functions.findec(driver, Locator.buttonNew)
    element.click()







    pass

