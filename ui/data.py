class Settings:
    baseurl = "http://mir.local/"
    login = "admin@mirmis.ru"
    password = "12345678"
    standarttime = 10


class Locator:
    InputLogin = "// input[@id='email']"
    inputPassword = "// input[@id='password']"
    buttonIn = "//*[ contains (text(), 'Войти' ) ]"
    buttonGVI = "// div[@class='content'] // *[ contains (text(), 'Главный врач' ) ]"
    buttonAdd = "// span[ contains (text(), 'Добавить' ) ]"
    inputPsurname = "// input[@id='patient_surname']"
    inputPname = "// input[@id='patient_name']"
    buttonSearch = "// div[@class='form-row'] // *[ contains (text(), 'Поиск' ) ]"
    buttonNew = "// p[ contains (text(), 'Создать' ) ]"
    selectRol = "// div[@class='user-info']"
    selectorGVI = "// div[@class='user-block__role'] // div[ contains (text(), 'Главный врач' ) ]"
    surnamePatientOD = "// input[@id='last_name']"
    firstnamePatientOD = "// input[@id='first_name']"
    middlenamePatientOD = "// input[@id='middle_name']"
    birthdatePatientOD = "// input[@id='birth_date']"
    selectMaleDB = "// p[ contains (text(), 'М' ) ]"
    inputWeightDB = "// input[@id='weight']"
    inputHeightDB = "// input[@id='height']"
    bloodgroupDB = "// div[@id='blood_group'] // div[@class='select-area']"
    bloodSelectDB = "// div[@id='blood_group'] // div[@class='select-area'] / div[2] / div[2]"
    selectGroupBloodDB = "// span[contains(text(), 'Rh(D)+')]"
    inputcountrySelect = "// div[@class='input-group']  // input"
    selectcountrySelect = "// *[ contains (text(), 'Россия' ) ]"
    socPolGroupDB = "// div[@id='social_status']  // div[@class='d-flex']"
    socPolSelectDB = "// div[@class='select-area']  // div[ contains (text(), 'Прочие' ) ]"
    semPolGroupDB = "// div[@id='family']  // div[@class='d-flex']"
    semPolSelectDB = "// div[@class='select-area']  // div[ contains (text(), 'Женат' ) ]"
    placeDB = "// input[@id='birth_place']"
    jobDB = "// input[@id='work_place']"
    moDB = "// input[@id='patient_institution']"
    phoneDB = "// input[@name='telephone']"
    descriptionPhoneDB = "// input[@name='description_phone']"
    emailDB = "// input[@id='email']"
    descriptionEmailDB = "// input[@id='email_note']"
    saveDataPatientDB = "// span[ contains (text(), 'Сохранить изменения' ) ]"
    docH3 = "// h3[ contains (text(), 'Документы' ) ]"
    addNewDoc = "// div[@class='add_new_document']"
    passportCit = "// p[ contains (text(), 'Паспорт гражданина РФ' ) ]"
    inputPassportSeries = "// input[@id='series']"
    inputPassportNumber = "// input[@id='number']"
    tareaPlaceTakePas = "// *[@id='issue_place']"
    inputDateTakePas = "// input[@id='issue_date']"
    inputCodDepTakePas = "// input[@id='division_code']"
    savePassport = "// div[@class='doc_forms_close'] // span[ contains (text(), 'Сохранить' ) ]"
    causeEdit = "// textarea[@class='form-control']"
    EditSave = "// div[@class='record-update-modal__body'] // span[ contains (text(), 'Сохранить' ) ]"
    zagranPas = "// p[ contains (text(), 'Заграничный паспорт' ) ]"
    passportGoden = "// input[@id='expiration_date']"
    passportCode = "// input[@id='personal_code']"
    svidORoj = " // p[ contains (text(), 'Свидетельство о рождении' ) ]"
    SNILS = "// p[ contains (text(), 'СНИЛС' ) ]"
    INN = "// p[ contains (text(), 'ИНН' ) ]"























