from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.input_first_name = (By.ID, "billing_first_name")
        self.input_second_name = (By.ID, "billing_last_name")
        self.input_country = (By.ID, "select2-billing_country-container")
        self.input_adress = (By.ID, "billing_address_1")
        self.input_city = (By.ID, "billing_city")
        self.input_state = (By.ID, "billing_state")
        self.input_postcode = (By.ID, "billing_postcode")
        self.input_phone = (By.ID, "billing_phone")
        self.radio_button = (By.ID, "payment_method_bacs")
        self.button_buy = (By.ID, "place_order")
        self.checkbox = (By.ID, "terms")

    def сheckout(self):
        self.driver.get("http://pizzeria.skillbox.cc/checkout/")
        self.driver.find_element(*self.input_first_name).send_keys("first_name")
        self.driver.find_element(*self.input_second_name).send_keys("second_name")
        self.driver.find_element(*self.input_adress).send_keys("adress")
        self.driver.find_element(*self.input_city).send_keys("city")
        self.driver.find_element(*self.input_state).send_keys("state")
        self.driver.find_element(*self.input_postcode).send_keys("postcode")
        self.driver.find_element(*self.input_phone).send_keys("+79999999999")
        self.driver.find_element(*self.radio_button).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.button_buy).click()
