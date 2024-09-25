from selenium.webdriver.common.by import By


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.button_auth = (By.CSS_SELECTOR, "button.woocommerce-form-login__submit")
        self.input_username = (By.ID, "username")
        self.input_password = (By.ID, "password")

    def login(self, login, password):
        self.driver.get("http://pizzeria.skillbox.cc/my-account/")
        self.driver.find_element(*self.input_username).send_keys(login)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.button_auth).click()
