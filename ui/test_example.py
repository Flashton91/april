import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

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

    functions.createPatientDoc(driver, Locator.passportCit)
    functions.findec(driver, Locator.inputDocSeries, userData["passportSerial"])
    functions.findec(driver, Locator.inputDocNumber, userData["passportNumber"])
    functions.findec(driver, Locator.tareaPlaceTakeDoc, userData["placeTakePas"])
    functions.findec(driver, Locator.inputDateTakeDoc, userData["vidan"])
    functions.findec(driver, Locator.inputCodDepTakePas, userData["codDepTakePas"])
    functions.savePatientDoctDoc(driver)

    functions.createPatientDoc(driver, Locator.zagranPas)
    functions.findec(driver, Locator.inputDocSeries, userData["zagranPassSeries"])
    functions.findec(driver, Locator.inputDocNumber, userData["zagranPassNumber"])
    functions.findec(driver, Locator.tareaPlaceTakeDoc, userData["placeTakeZagran"])
    functions.findec(driver, Locator.inputDateTakeDoc, userData["vidan"])
    functions.findec(driver, Locator.passportGoden, userData["godenDo"])
    functions.findec(driver, Locator.passportCode, userData["personalCodesZagran"])
    functions.savePatientDoctDoc(driver)

    functions.createPatientDoc(driver, Locator.svidORj)
    functions.findec(driver, Locator.inputDocSeries, "I-ЕА")
    functions.findec(driver, Locator.inputDocNumber, userData["NumberSvidOR"])
    functions.findec(driver, Locator.tareaPlaceTakeDoc, userData["placeSvidOR"])
    functions.findec(driver, Locator.inputDateTakeDoc, userData["vidan"])
    functions.savePatientDoctDoc(driver)

    functions.createPatientDoc(driver, Locator.SNILS)
    functions.findec(driver, Locator.inputDocNumber, userData["SNILS"])
    functions.savePatientDoctDoc(driver)

    functions.createPatientDoc(driver, Locator.INN)
    functions.findec(driver, Locator.inputDocNumber, userData["INN"])
    functions.findec(driver, Locator.inputDateTakeDoc, userData["vidan"])
    functions.savePatientDoctDoc(driver)

    functions.createPatientDoc(driver, Locator.voennik)
    functions.findec(driver, Locator.inputDocSeries, "АС")
    functions.findec(driver, Locator.inputDocNumber, userData["numberVoennik"])
    functions.findec(driver, Locator.tareaPlaceTakeDoc, userData["placeTakePas"])
    functions.findec(driver, Locator.inputDateTakeDoc, userData["vidan"])
    functions.findec(driver, Locator.voennikSpec, "Танкист")
    functions.savePatientDoctDoc(driver)

    functions.createPatientDoc(driver, Locator.vidNaJit)
    functions.findec(driver, Locator.inputDocSeries, "82")
    functions.findec(driver, Locator.inputDocNumber, userData["vidNaJit"])
    functions.findec(driver, Locator.numberReshVidNaJit, userData["numRVidNaJit"])
    functions.findec(driver, Locator.dataReshVidNaJit, userData["vidan"])
    functions.findec(driver, Locator.inputDateTakeDoc, userData["vidan"])
    functions.findec(driver, Locator.godnoVidNaJit, userData["godenDo"])
    functions.savePatientDoctDoc(driver)
    time.sleep(3)

    assert functions.yot(driver, "// div[@class='row'] // h3[ contains (text(), 'Паспорт гражданин РФ' ) ]")
    assert functions.yot(driver, "// div[@class='row'] // h3[ contains (text(), 'Заграничный паспорт' ) ]")
    assert functions.yot(driver, "// div[@class='row'] // h3[ contains (text(), 'Свидетельство о рождении' ) ]")

    assert functions.yot(driver, "// div[@class='row'] // h3[ contains (text(), 'ИНН' ) ]")

    assert functions.yot(driver, "// div[@class='row'] // h3[ contains (text(), 'Военный билет' ) ]")
    assert functions.yot(driver, "// div[@class='row'] // h3[ contains (text(), 'Вид на жительство' ) ]")


