import allure
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.input_search = (By.CLASS_NAME, "search-field")
        self.button_search = (By.XPATH, "//button[@class = 'searchsubmit']")

    def go_to_search(self):
        with allure.step("переход на главную страницу"):
            self.driver.get("http://pizzeria.skillbox.cc/")
        with allure.step("Ввод в поиск "):
            self.driver.find_element(*self.input_search).send_keys("пепперони")
        with allure.step('Нажатие кнопки "Поиск"'):
            self.driver.find_element(*self.button_search).click()
