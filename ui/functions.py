import random
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
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
        return element
    if action == "PressEnter":
        time.sleep(10)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.UP)
        element.send_keys(Keys.ENTER)
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

def generateUserDataRnd():
    userData = {}
    nameList = ("Григорий", "Лев", "Андрей", "Роман", "Арсений", "Степан", "Владислав", "Никита", "Глеб", "Марк", "Давид", "Ярослав", "Евгений", "Матвей", "Фёдор", "Николай", "Алексей", "Андрей", "Артемий", "Виктор", "Никита", "Даниил", "Денис", "Егор", "Игорь", "Лев", "Леонид", "Павел", "Петр")
    surnameList = ("Смирнов", "Иванов", "Кузнецов", "Соколов", "Попов", "Лебедев", "Козлов", "Новиков", "Морозов", "Петров", "Волков", "Соловьёв", "Васильев", "Зайцев", "Павлов", "Семёнов", "Голубев", "Виноградов", "Богданов", "Воробьёв", "Фёдоров", "Михайлов", "Беляев", "Тарасов", "Белов", "Комаров", "Орлов", "Киселёв", "Макаров")
    middlenameList = ("Алексеевич", "Анатольевич", "Андреевич", "Антонович", "Аркадьевич", "Бедросович", "Богданович", "Борисович", "Валентинович", "Валерьевич", "Васильевич", "Викторович", "Витальевич", "Владимирович", "Владиславович", "Вольфович", "Вячеславович", "Геннадиевич", "Георгиевич", "Григорьевич", "Данилович", "Денисович", "Дмитриевич", "Евгеньевич", "Егорович", "Ефимович", "Иванович", "Иваныч", "Игнатьевич")
    placeList = ("Московская область, г. Балахиша, ул. Ленина, д. 35, кв. 11", "Свердловская область, г. Краснотурьинск, ул. Ленина, д. 15, кв. 2", "Челябинская область, г. Магнитогорск, ул. Ленина, д. 20б кв. 5")
    jobList = ("ООО Газмяс", "ЗАО Землеком", "ФГУП ФНПЦ Рассвет", "ЗАО Севкабель", "ООО Водоканал")
    moJoinList = ("МСЧ-59", "КБУЗ Ивановская поликлиника", "КГБУЗ Ленинская районная больница")
    placeTakePasList = ("ОТДЕЛ ВНУТРЕННИХ ДЕЛ ГОЛЬЯНОВО ГОРОДА МОСКВЫ", "ОТДЕЛ ОУФМС ПО РЕСПУБЛИКЕ ТАТАРСТАН В ГОРОДЕ КАЗАНЬ", "ОТДЕЛ ВНУТРЕННИХ ДЕЛ ОДИНЦОВСКОГО РАЙОНА ГОРОДА МОСКВЫ")
    snilsList = ("24421369850", "06566568405", "38644102791", "20035186404", "12982147277")
    userData["name"] = random.choice(nameList)
    userData["surname"] = random.choice(surnameList)
    userData["middlename"] = random.choice(middlenameList)
    userData["phone"] = '8909317' +  str(random.randint(1000,9999))
    userData["borndate"] = str(random.randint(10,29)) + str(random.randint(10,12)) + str(random.randint(1950,2000))
    userData["weight"] = str(random.randint(70,180))
    userData["height"] = str(random.randint(160, 200))
    userData["place"] = random.choice(placeList)
    userData["job"] = random.choice(jobList)
    userData["moJoin"] = random.choice(moJoinList)
    userData["email"] = "test" + str(random.randint(1, 100)) + "@test.com"
    userData["passportSerial"] = str(random.randint(10, 99)) + str(random.randint(10, 99))
    userData["passportNumber"] = str(random.randint(100000, 999999))
    userData["placeTakePas"] = random.choice(placeTakePasList)
    userData["dateTakePas"] = str(random.randint(10,29)) + str(random.randint(10,12)) + str(random.randint(1990,2000))
    userData["codDepTakePas"] = str(random.randint(100, 999)) + '-' + str(random.randint(100, 999))
    userData["zagranPassSeries"] = str(random.randint(10,99))
    userData["zagranPassNumber"] = str(random.randint(100, 999)) + str(random.randint(1000, 9999))
    userData["placeTakeZagran"] = random.choice(placeTakePasList)
    userData["dateTakeZagran"] = str(random.randint(10,29)) + str(random.randint(10,12)) + str(random.randint(2015,2023))
    userData["godenDateZagran"] = str(random.randint(10,29)) + str(random.randint(10,12)) + str(random.randint(2026, 2030))
    userData["personalCodesZagran"] = str(random.randint(100000, 999999))
    userData["NumberSvidOR"] = str(random.randint(100000, 999999))
    userData["placeSvidOR"] = random.choice(moJoinList)
    userData["dateSvidOR"] = str(random.randint(10,29)) + str(random.randint(10,12)) + str(random.randint(1950,2000))
    userData["SNILS"] = random.choice(snilsList)
    userData["INN"] = str(random.randint(1000,9999)) + str(random.randint(1000,9999)) + str(random.randint(1000,9999))
    userData["dateINN"] = str(random.randint(10,29)) + str(random.randint(10,12)) + str(random.randint(2015,2022))
    return userData

