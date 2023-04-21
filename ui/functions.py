from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import Settings, Locator
from selenium.webdriver.support import expected_conditions as EC
def findec(driver, locator):
    wait = WebDriverWait(driver, timeout=20, poll_frequency=1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
    return element

def scrollDown(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return driver