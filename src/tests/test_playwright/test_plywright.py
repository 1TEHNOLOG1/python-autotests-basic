import allure
from playwright.sync_api import Page


def test_search(page: Page):
    with allure.step("Переход на страницу"):
        page.goto("https://github.com/microsoft/vscode/issues")
    with allure.step('Ввод в поиск "in:title bug"'):
        page.fill("#js-issues-search", "in:title bug")
    with allure.step("Поиск результатов"):
        page.press("#js-issues-search", "Enter")
        page.wait_for_selector("#issue_223805_link", timeout=3000)
    with allure.step('Проверка отображения задач, которые содержат "bug" в названии'):
        issues = page.query_selector_all('a[data-hovercard-type="issue"]')
        assert all("bug" in issue.text_content().lower() for issue in issues)


def test_input_author(page: Page):
    with allure.step("Переход на страницу"):
        page.goto(" https://github.com/microsoft/vscode/issues")
    with allure.step("Нажатие на кнопку Author"):
        page.click('//*[@title="Author"]')
    with allure.step('Ввод в поле поиска "bpasero"'):
        page.fill("#author-filter-field", "bpasero")
        page.wait_for_selector("#author-filter-field", timeout=3000)
    with allure.step("Выбор автора в выпадающем списке"):
        page.click("//*[@value = 'bpasero']")
    with allure.step("Проверка, что автор введен в поиск"):
        el = page.input_value("#js-issues-search")
        assert "bpasero" in el


def test_check_stars(page: Page):
    with allure.step("Переход на страницу"):
        page.goto("https://github.com/search/advanced")
    with allure.step("выбор поля языка програмирования"):
        page.click("#search_language")
    with allure.step("Выбор языка python"):
        page.select_option("#search_language", "Python")
    with allure.step('Ввод в поле ">20000"'):
        page.fill("#search_stars", ">20000")
    with allure.step('Ввод в поле "environment.yml"'):
        page.fill("#search_filename", "environment.yml")
    with allure.step("Переход на страницу"):
        page.click(".btn.flex-auto")

    with allure.step("Проверка звезд в репозиториях "):
        with allure.step("Проверка звезд в репозиториях"):
            stars = [
                int(element.get_attribute("aria-label").split()[0]) > 20000
                for element in page.query_selector_all(
                    "//*[contains(@aria-label,'stars')]"
                )
            ]
            print(stars)
            assert all(stars)


def test_skillbox_profession(page: Page):
    with allure.step("Переход на страницу"):
        page.goto("https://skillbox.ru/code/", wait_until="load")
    with allure.step('Выбор радиобаттона "Профессия"'):
        page.click('//*[@value="profession"]')
    with allure.step("Устновка диапазона от 6 месяцев до 12 месяцев"):
        el_1 = page.locator('//*[@class="ui-range__dot"])[1]')
        el_2 = page.locator('(//*[@class="ui-range__dot"])[2]')
        page.mouse.click(el_1.bounding_box()["x"], el_1.bounding_box()["y"])
        page.mouse.move(el_1.bounding_box()["x"] + 50, el_1.bounding_box()["y"])
        page.mouse.click(el_2.bounding_box()["x"], el_2.bounding_box()["y"])
        page.mouse.move(el_2.bounding_box()["x"] - 60, el_2.bounding_box()["y"])
    with allure.step("Выбор чек-бокса"):
        page.click("//span[contains(text(), 'Android')]")
    page.wait_for_selector(
        "//*[@class = 'courses-block courses-section__block']", timeout=3000
    )
    profession1 = page.text_content(
        "(//*[@class = 'ui-product-card-main__title t t--2'])[1]"
    )
    profession2 = page.text_content(
        "(//*[@class = 'ui-product-card-main__title t t--2'])[2]"
    )
    with allure.step("Проверка найденных профессий"):
        assert profession1 == "Android-разработчик"
        assert profession2 == "Мобильный разработчик"


def test_tooltip(page: Page):
    with allure.step("Переход на страницу"):
        page.goto("https://github.com/microsoft/vscode/graphs/commit-activity")

    with allure.step("Наведение курсора на график"):
        graph = page.locator('//*[@height="100"]')
        graph.hover()
    page.wait_for_selector("(//*[contains(text(), 'commits')])[2]", timeout=3000)

    tooltip = page.locator(".svg-tip").text_content()
    with allure.step("Проверка tooltip"):
        assert tooltip == "381 commits the week of Sep 3"
