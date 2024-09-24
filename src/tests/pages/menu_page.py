import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.tests.conftest import set_up_browser


class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.button_add_item = (By.XPATH, "//*[contains(@data-product_id, '427')]")
        self.button_cart = (By.CLASS_NAME, 'view-cart')
        self.slider_1 = (By.XPATH, "(//span[@class ='ui-slider-handle ui-state-default ui-corner-all'])[1]")
        self.slider_2 = (By.XPATH, "(//div/span[last()])[15]")
        self.button_filter = (By.XPATH, "//button[@class ='button']")

    def menu_page(self):
        self.driver.get('http://pizzeria.skillbox.cc/product-category/menu/')

    def add_to_cart(self):
        self.driver.find_element(*self.button_add_item).click()

    def go_to_cart(self):
        time.sleep(5)  # TODO: Убрать после исправления бага на беке
        self.driver.find_element(*self.button_cart).click()

    def filter_price(self):
        actions = ActionChains(self.driver)
        slider_1_element = self.driver.find_element(*self.slider_1)
        actions.click_and_hold(slider_1_element).move_by_offset(xoffset=50, yoffset=0).perform()
        slider_2_element = self.driver.find_element(*self.slider_2)
        actions.click_and_hold(slider_2_element).move_by_offset(xoffset=-50, yoffset=0).perform()
        self.driver.find_element(*self.button_filter).click()


