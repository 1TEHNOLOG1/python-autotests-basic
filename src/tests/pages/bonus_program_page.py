import allure
from selenium.webdriver.common.by import By


class BonusProgram:
    def __init__(self, driver):
        self.driver = driver
        self.input_name = (By.ID, "bonus_username")
        self.input_phone = (By.ID, "bonus_phone")
        self.button_apply = (By.XPATH, "//*[contains(text(), 'Оформить карту')]")

    def bonus_program(self, name, phone):
        with allure.step('Переход на страницу'):
            self.driver.get('http://pizzeria.skillbox.cc/bonus/')
        with allure.step('Заполнение поля - Имя'):
            self.driver.find_element(*self.input_name).send_keys(name)
        with allure.step('Заполнение поля - Телефон'):
            self.driver.find_element(*self.input_phone).send_keys(phone)
        with allure.step('Нажатие кнопки '):
            self.driver.find_element(*self.button_apply).click()
