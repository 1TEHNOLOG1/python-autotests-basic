import time

from selenium.webdriver.common.by import By


class BucketPage:
    def __init__(self, driver):
        self.driver = driver
        self.button_use_coupon = (By.XPATH, "//button[@value = 'Применить купон']")
        self.button_update_backed = (By.XPATH, "//button[@value = 'Обновить корзину']")
        self.button_pay = (By.CLASS_NAME, "checkout-button button alt wc-forward")
        self.button_delite = (By.CSS_SELECTOR, '.remove.remove')

    def go_to_bucket(self):
        time.sleep(5)  # TODO: Убрать после исправления бага на беке
        self.driver.get("http://pizzeria.skillbox.cc/cart/")

    def backed_page(self):
        time.sleep(5)  # TODO: Убрать после исправления бага на беке
        self.driver.get('http://pizzeria.skillbox.cc/cart/')
        self.driver.find_element(*self.button_update_backed).click()
        self.driver.find_element(*self.button_pay).click()

    def use_coupon(self, promo_code):
        time.sleep(3)  # TODO: Убрать после исправления бага на беке
        self.driver.find_element(By.ID, "coupon_code").send_keys(promo_code)
        self.driver.find_element(By.NAME, 'apply_coupon').click()

    def delite_item(self):
        self.driver.find_element(*self.button_delite).click()

    def get_original_price(self):
        original_price = self.driver.find_element(By.XPATH,
                                                  "(//span[@class ='woocommerce-Price-amount amount'])[3]").text
        original_price = float(original_price.replace('₽', '').replace(',', '.'))
        return original_price

    def get_final_price(self):
        final_price = self.driver.find_element(By.XPATH, "(//span[@class ='woocommerce-Price-amount amount'])[5]").text
        final_price = float(final_price.replace('₽', '').replace(',', '.'))
        return final_price

