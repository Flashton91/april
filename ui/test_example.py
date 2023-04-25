import time

from selenium.webdriver import Keys

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
    userData = functions.generateUserDataRnd()
    print(userData)
    functions.findec(driver, Locator.surnamePatientOD, userData["surname"])
    functions.findec(driver, Locator.firstnamePatientOD, userData["name"])
    functions.findec(driver, Locator.middlenamePatientOD, userData["middlename"])
    functions.findec(driver, Locator.birthdatePatientOD, userData["borndate"])
    functions.findec(driver, Locator.selectMaleDB, "PressElement")
    functions.findec(driver, Locator.inputWeightDB, userData["weight"])
    functions.findec(driver, Locator.inputHeightDB, userData["height"])
    functions.findec(driver, Locator.bloodgroupDB, "PressElement")
    functions.findec(driver, Locator.bloodSelectDB, "PressElement")
    time.sleep(10)
    functions.findec(driver, Locator.inputcountrySelect, "PressElement")

    functions.findec(driver, Locator.inputcountrySelect, "PressEnter")
    functions.findec(driver, Locator.socPolGroupDB, "PressElement")
    functions.findec(driver, Locator.socPolSelectDB, "PressElement")
    functions.findec(driver, Locator.semPolGroupDB, "PressElement")
    functions.findec(driver, Locator.semPolSelectDB, "PressElement")
    functions.findec(driver, Locator.placeDB, userData["place"])
    functions.findec(driver, Locator.jobDB, userData["job"])
    functions.findec(driver, Locator.moDB, userData["moJoin"])
    functions.findec(driver, Locator.phoneDB, userData["phone"])
    functions.findec(driver, Locator.descriptionPhoneDB, "Мобильный телефон")
    functions.findec(driver, Locator.emailDB, userData["email"])
    functions.findec(driver, Locator.descriptionEmailDB, "Почта пациента")
    functions.findec(driver, Locator.saveDataPatientDB, "PressElement")
    functions.scrollDown(driver)

    functions.findec(driver, Locator.docH3, "PressElement")
    functions.findec(driver, Locator.addNewDoc, "PressElement")
    functions.findec(driver, Locator.passportCit, "PressElement")
    functions.findec(driver, Locator.inputPassportSeries, userData["passportSerial"])
    functions.findec(driver, Locator.inputPassportNumber, userData["passportNumber"])
    functions.findec(driver, Locator.tareaPlaceTakePas, userData["placeTakePas"])
    functions.findec(driver, Locator.inputDateTakePas, userData["dateTakePas"])
    functions.findec(driver, Locator.inputCodDepTakePas, userData["codDepTakePas"])
    functions.findec(driver, Locator.savePassport, "PressElement")
    functions.findec(driver, Locator.causeEdit, "Тест")
    functions.findec(driver, Locator.EditSave, "PressElement")

    functions.findec(driver, Locator.addNewDoc, "PressElement")
    functions.findec(driver, Locator.zagranPas, "PressElement")
    functions.findec(driver, Locator.inputPassportSeries, userData["zagranPassSeries"])
    functions.findec(driver, Locator.inputPassportNumber, userData["zagranPassNumber"])
    functions.findec(driver, Locator.tareaPlaceTakePas, userData["placeTakeZagran"])
    functions.findec(driver, Locator.inputDateTakePas, userData["dateTakeZagran"])
    functions.findec(driver, Locator.passportGoden, userData["godenDateZagran"])
    functions.findec(driver, Locator.passportCode, userData["personalCodesZagran"])
    functions.findec(driver, Locator.savePassport, "PressElement")
    functions.findec(driver, Locator.causeEdit, "Тест")
    functions.findec(driver, Locator.EditSave, "PressElement")

    functions.findec(driver, Locator.addNewDoc, "PressElement")
    functions.findec(driver, Locator.svidORoj, "PressElement")
    functions.findec(driver, Locator.inputPassportSeries, "I-ЕА")
    functions.findec(driver, Locator.inputPassportNumber, userData["NumberSvidOR"])
    functions.findec(driver, Locator.tareaPlaceTakePas, userData["placeSvidOR"])
    functions.findec(driver, Locator.inputDateTakePas, userData["dateSvidOR"])
    functions.findec(driver, Locator.savePassport, "PressElement")
    functions.findec(driver, Locator.causeEdit, "Тест")
    functions.findec(driver, Locator.EditSave, "PressElement")

    functions.findec(driver, Locator.addNewDoc, "PressElement")
    functions.findec(driver, Locator.SNILS, "PressElement")
    functions.findec(driver, Locator.inputPassportNumber, userData["SNILS"])
    functions.findec(driver, Locator.savePassport, "PressElement")
    functions.findec(driver, Locator.causeEdit, "Тест")
    functions.findec(driver, Locator.EditSave, "PressElement")

    functions.findec(driver, Locator.addNewDoc, "PressElement")
    functions.findec(driver, Locator.INN, "PressElement")
    functions.findec(driver, Locator.inputPassportNumber, userData["INN"])
    functions.findec(driver, Locator.inputDateTakePas, userData["dateINN"])
    functions.findec(driver, Locator.savePassport, "PressElement")
    functions.findec(driver, Locator.causeEdit, "Тест")
    functions.findec(driver, Locator.EditSave, "PressElement")




    time.sleep(30)

    pass

