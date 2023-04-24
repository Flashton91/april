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



