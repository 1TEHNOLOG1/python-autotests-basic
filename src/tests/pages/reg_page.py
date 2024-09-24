import random
import string
import allure
from selenium.webdriver.common.by import By


class RegistPage:
    def __init__(self, driver):
        self.driver = driver
        self.button_reg = (By.CSS_SELECTOR, 'p>.button')
        self.input_email = (By.ID, 'reg_email')
        self.reg_username = (By.ID, 'reg_username')
        self.input_password = (By.ID, 'reg_password')

    def user_registration(self, username, mail, password):
        self.driver.get('https://pizzeria.skillbox.cc/register/')
        with allure.step('Ввод в поле Имя'):
            self.driver.find_element(*self.reg_username).send_keys(username)
        with allure.step('Ввод в поле mail'):
            self.driver.find_element(*self.input_email).send_keys(mail)
        with allure.step('Ввод в поле - пароль'):
            self.driver.find_element(*self.input_password).send_keys(password)
        with allure.step('Нажатие кнопки - Зарегистрироваться'):
            self.driver.find_element(*self.button_reg).click()

    def random_user_reg(self):
        random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        mail = random_string + '@mail.ru'
        self.user_registration(username=random_string, mail=mail, password=random_string)
        return random_string, random_string
