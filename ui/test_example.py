import time

import functions
from data import Settings, Locator
from selenium import webdriver

def test_ex(driver):
    functions.roleSelectGVI(driver)
    driver.get(Settings.baseurl + "medical-studies")
    functions.findec(driver, Locator.buttonAdd, "PressElement")
    functions.findec(driver, Locator.inputPsurname, "ВместоИмя")
    functions.findec(driver, Locator.inputPname, "ВместоФамилии")
    functions.findec(driver, Locator.buttonSearch, "PressElement")
    functions.scrollDown(driver)
    functions.findec(driver, Locator.buttonNew, "PressElement")









    pass

