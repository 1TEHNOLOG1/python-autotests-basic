import allure
from playwright.sync_api import Page


def test_block_requests_use_promo(page: Page):
    with allure.step("Переход на страницу"):
        page.goto("http://pizzeria.skillbox.cc/product-category/menu/")
    with allure.step("добавление товара в корзину"):
        page.click("//*[contains(@data-product_id, '427')]")
        page.wait_for_timeout(5000)
    with allure.step("Переход на страницу - Корзина"):
        page.goto("http://pizzeria.skillbox.cc/cart/")
    with allure.step("Применение купона"):
        page.fill("#coupon_code", "GIVEMEHALYAVA")
    with allure.step("Нажати кнопки - применить купон"):
        page.click("//button[contains(text(), 'Применить купон')]")
    with allure.step("Блок запроса на применение купона "):
        page.route("**?wc - ajax = apply_coupon", lambda route: route.abort())
    with allure.step("Проверка неприменения купона"):
        original_price = page.locator("(//bdi)[3]").inner_text()
        original_price = float(original_price.replace("₽", "").replace(",", "."))
        final_price = page.locator("(//bdi)[4]").inner_text()
        print(original_price, final_price)
        final_price = float(final_price.replace("₽", "").replace(",", "."))
        assert final_price == original_price
