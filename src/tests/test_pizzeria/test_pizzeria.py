import time
import pytest
from selenium.webdriver.common.by import By
import allure
from src.tests.pages.auth_page import AuthPage
from src.tests.pages.backed_page import BucketPage
from src.tests.pages.base_page import BasePage
from src.tests.pages.bonus_program_page import BonusProgram
from src.tests.pages.checkout_page import CheckoutPage
from src.tests.pages.menu_page import MenuPage
from src.tests.pages.reg_page import RegistPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPizza:
    def test_registration(self, set_up_browser):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
        with allure.step('Регистрация'):
            reg_page = RegistPage(driver)
            reg_page.random_user_reg()
        with allure.step('Проверка регистрации'):
            logout = driver.find_element(By.XPATH, "//a[@class = 'logout']").text
            reg = driver.find_element(By.XPATH, "//div[@class = 'content-page']").text
            assert reg == 'Регистрация завершена'
            assert logout == 'Выйти'

    def test_authorization(self, set_up_browser):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
        with allure.step('Переход на страницу авторизации'):
            auth_page = AuthPage(driver=driver)
        with allure.step('Авторизация'):
            registr = RegistPage(driver)
            login, password = registr.random_user_reg()
            auth_page.login(login, password)
        with allure.step('Проверка авторизации'):
            logout = driver.find_element(By.XPATH, "//a[@class = 'logout']").text
            assert logout == 'Выйти'
    #     Доделать

    def test_use_promo(self, set_up_browser):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
        with allure.step('Переход на страницу'):
            menu_page = MenuPage(driver)
            menu_page.menu_page()
        with allure.step('Добавление товаров в корзину'):
            menu_page.add_to_cart()
        with allure.step('Перехoд на страницу оформления товаров'):
            bucket_page = BucketPage(driver)
            bucket_page.go_to_bucket()
        with allure.step('Применение купона'):
            bucket_page = BucketPage(driver)
            bucket_page.use_coupon('GIVEMEHALYAVA')
        with allure.step('Проверка применения купона '):
            assert bucket_page.get_final_price() == bucket_page.get_original_price() * 0.90


    def test_use_invalid_promo(self, set_up_browser):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
            menu_page = MenuPage(driver)
        with allure.step('Переход на страницу меню'):
            menu_page.menu_page()
        with allure.step('Добавление товара в корзину'):
            menu_page.add_to_cart()
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((
                By.XPATH, "//div[@class='inner']"
            )))
            BucketPage(driver)
            bucket_page = BucketPage(driver)
            bucket_page.go_to_bucket()
            bucket_page.use_coupon('DC120')
        with allure.step('Проверка применения купона '):
            original_price = driver.find_element(By.XPATH,
                                                 "(//span[@class ='woocommerce-Price-amount amount'])[2]").text
            original_price = float(original_price.replace('₽', '').replace(',', '.'))
            final_price = driver.find_element(By.XPATH, "(//span[@class ='woocommerce-Price-amount amount'])[3]").text
            final_price = float(final_price.replace('₽', '').replace(',', '.'))
            expected_price = original_price
            assert final_price == expected_price
            alert = driver.find_element(By.XPATH, "//*[contains(@class,'woocommerce-error')]").text
            assert alert == 'Неверный купон.'

    @pytest.mark.skip(reason = 'Купон применятся дважды для одного пользователя')
    def test_double_use_promo(self, set_up_browser):
        driver = set_up_browser
        menu_page = MenuPage(driver)
        AuthPage(driver)
        with allure.step('Регистрация'):
            reg_page = RegistPage(driver)
            reg_page.random_user_reg()
        with allure.step('Добавление товаров в корзину'):
            menu_page.menu_page()
            menu_page.add_to_cart()
            WebDriverWait(driver, 3).until((EC.presence_of_element_located((
                By.XPATH, "//div[@class='inner']"
            ))))
        with allure.step('Переход на страницу-Корзина'):
            menu_page.go_to_cart()
            bucket_page = BucketPage(driver)
        with allure.step('Применение  валидного промокода'):
            bucket_page.use_coupon('GIVEMEHALYAVA')
        with allure.step('Заполнение формы оформления заказа'):
            checkout_page = CheckoutPage(driver)
            checkout_page.сheckout()
            WebDriverWait(driver, 3).until((EC.presence_of_element_located((
                By.XPATH, "//h2[contains(text(), 'Заказ получен')]"
            ))))
        with allure.step('Проверка применения промокода'):
            assert 'ЗАКАЗ ПОЛУЧЕН' in driver.find_element(By.XPATH, "//h2[@class='post-title']").text

        with allure.step('Добавление товаров в корзину повторно'):
            menu_page.menu_page()
            menu_page.add_to_cart()
            WebDriverWait(driver, 3).until((EC.presence_of_element_located((
                By.XPATH, "//div[@class='inner']"
            ))))
        with allure.step('Переход на страницу-Корзина повторно'):
            menu_page.go_to_cart()
        bucket_page = BucketPage(driver)
        with allure.step('Применение  валидного промокода повторно'):
            bucket_page.use_coupon('GIVEMEHALYAVA')
        with allure.step('Заполнение формы оформления заказа повторно'):
            checkout_page = CheckoutPage(driver)
            checkout_page.сheckout()
            WebDriverWait(driver, 3).until((EC.presence_of_element_located((
                By.XPATH, "//div[@class='content-inner clearfix']"
            ))))
        with allure.step('Проверка применения промокода'):
            assert 'Coupon code already applied! ' in driver.find_element(
                By.XPATH, "//li[contains(text(),'Coupon code already applied!')]"
            )

    def test_bonus_program(self, set_up_browser):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
            bonus_program = BonusProgram(driver)
            bonus_program.bonus_program(name='aleks', phone='+79960014897')
            driver.switch_to.alert.accept()
            WebDriverWait(set_up_browser, 10).until(EC.visibility_of_element_located((
                By.XPATH, "//div/div/h3")))
        with allure.step('Проверка'):
            assert 'Ваша карта оформлена!' in driver.find_element(By.ID, 'bonus_main').text

    def test_bonus_program_double(self, set_up_browser):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
        bonus_program = BonusProgram(driver)
        bonus_program.bonus_program(name='aleks', phone='+79960014897')
        with allure.step('Проверка'):
            driver.switch_to.alert.accept()
            assert 'Ваша карта оформлена!' in driver.find_element(By.ID, 'bonus_main').text

    @pytest.mark.parametrize('phone', ['retdrghyjfd', '123'])
    def test_bonus_program_negativ(self, set_up_browser, phone):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
        with allure.step('Переход на страницу'):
            driver.get('http://pizzeria.skillbox.cc/bonus/')
        with allure.step('Заполнение полей - Имя и Телефон'):
            driver.find_element(By.ID, 'bonus_username').send_keys('Aleks')
            driver.find_element(By.ID, 'bonus_phone').send_keys(phone)
            driver.find_element(By.CSS_SELECTOR, 'div>button.button').click()
            time.sleep(2)
        with allure.step('Проверка'):
            assert 'Введен неверный формат телефона' in driver.find_element(By.ID, 'bonus_content').text

    def test_add_items_in_bucket(self, set_up_browser):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
        with allure.step('Авторизация'):
            auth_page = AuthPage(driver)
            auth_page.login(login='kiki11', password='kiki11')
        with allure.step('Добавлеине товара в корзину'):
            menu_page = MenuPage(driver)
            menu_page.menu_page()
            menu_page.add_to_cart()
            menu_page.go_to_cart()
            count_item = driver.find_element(By.XPATH, "//td[@class = 'product-name']")
        with allure.step('Проверка добавления товара в корзину'):
            assert count_item.is_displayed()
            print(count_item.text)

    def test_delite_items_in_backed(self, set_up_browser):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
        with allure.step('Переход на страницу авторизации'):
            auth_page = AuthPage(driver)
        with allure.step('Авторизация'):
            auth_page.login(login='kiki11', password='kiki11')
        with allure.step('Переход на страницу - меню'):
            menu_page = MenuPage(driver)
            menu_page.menu_page()
        with allure.step('Добавление товара в корзину'):
            menu_page.add_to_cart()
            time.sleep(3)
        with allure.step('Переход на страницу - корзина'):
            bucket_page = BucketPage(driver)
            bucket_page.go_to_bucket()
            WebDriverWait(set_up_browser, 2).until(EC.presence_of_element_located((By.ID, 'main')))
        with allure.step('Удаление товара из корзины'):
            bucket_page.delite_item()
        with allure.step('Проверка удаления товара из корзины'):
            assert driver.find_element(By.CSS_SELECTOR, 'p.cart-empty').text == 'Корзина пуста.'

    def test_search(self, set_up_browser):
        driver = set_up_browser
        base_page = BasePage(driver)
        base_page.go_to_search()
        with allure.step('Проверка результатов поиска '):
            assert driver.find_element(By.XPATH,
                                       "//h1[@class ='product_title entry-title']").text == 'Пицца «Пепперони»'

    def test_filter_price(self, set_up_browser):
        with allure.step('Запуск браузера'):
            driver = set_up_browser
        with allure.step('Переход на страницу - меню'):
            menu_page = MenuPage(driver)
            menu_page.menu_page()
        with allure.step('Сортировка товара по цене '):
            menu_page.filter_price()

        with allure.step('Проверка фильтрации товаров по цене'):
            price = driver.find_elements(By.XPATH, "//span[@class ='price']")
            WebDriverWait(set_up_browser, 3).until(EC.visibility_of_all_elements_located((
                By.XPATH, "//div[@class = 'wc-products']"
            )))
            normal_prices = [300.00, 300.00, 435.00, 450.00]
            result_prices = []
            for el in price:
                print(float(el.text.replace(',', '.').replace('₽', '')))
                result_prices.append(float(el.text.replace(',', '.').replace('₽', '')))
            assert sorted(normal_prices) == sorted(result_prices)

