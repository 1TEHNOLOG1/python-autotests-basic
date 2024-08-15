from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class TestCases:
    def test_case1(self, set_up_browser):
        driver = set_up_browser
        driver.get(" https://github.com/microsoft/vscode/issues")
        driver.find_element(By.ID, "js-issues-search").send_keys("in:title bug")
        driver.find_element(By.ID, "js-issues-search").send_keys(Keys.ENTER)
        WebDriverWait(set_up_browser, 3).until(EC.presence_of_element_located((By.ID, 'issue_223805_link')))
        issues = driver.find_elements(By.XPATH, '//a[@data-hovercard-type="issue"]')
        with allure.step('Проверка отображения задач, которое содержит "bug" в названии'):
            elements = ['bug' in element.text.lower() for element in issues]
            assert all(elements)

    def test_case2(self, set_up_browser):
        driver = set_up_browser
        driver.get(" https://github.com/microsoft/vscode/issues")
        driver.find_element(By.XPATH, '//*[@title="Author"]').click()
        driver.find_element(By.ID, "author-filter-field").send_keys("bpasero")
        WebDriverWait(set_up_browser, 3).until(EC.presence_of_element_located((By. XPATH, "//*[@class = "
                                                                                          "'js-navigation-container "
                                                                                          "js-active-navigation"
                                                                                          "-container']")))

        driver.find_element(
            By.XPATH,
            '//*[@class="SelectMenu-list select-menu-list is-showing-new-item-form"]',
        ).click()
        with allure.step('Проверка, что автор введен в поиск'):
            el = driver.find_element(By.ID, 'js-issues-search').get_attribute('value')
            assert 'bpasero' in el

    def test_case3(self, set_up_browser):

        driver = set_up_browser
        driver.get("https://github.com/search/advanced")
        driver.find_element(By.ID, "search_language").click()
        select_language = driver.find_element(By.XPATH, "//option[@value ='Python']").click()
        repo_options_stars = driver.find_element(By.ID, "search_stars").send_keys(">20000")
        code_options_file_name = driver.find_element(By.ID, "search_filename").send_keys("environment.yml")
        search = driver.find_element(By.CSS_SELECTOR, ".btn.flex-auto").click()
        repositories = driver.find_elements(By.CSS_SELECTOR, 'div[class="Box-sc-g0xbh4-0 hDWxXB]')
        with allure.step('Проверка звезд в репозиториях '):
            stars = [int(element.get_attribute("aria-label").split()[0]) > 20000 for element in driver.find_elements(By.XPATH,"//*[contains(@aria-label,'stars')]")]
            print(stars)
            assert all(stars)



    def test_case4(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        driver.get("https://skillbox.ru/code/")
        driver.find_element(By.XPATH, '//*[@value="profession"]').click()
        el_1 = driver.find_element(By.XPATH, '(//*[@class="ui-range__dot"])[1]')
        actions = ActionChains(driver)
        actions.click_and_hold(el_1).move_by_offset(xoffset=50, yoffset=0).perform()
        el_2 = driver.find_element(By.XPATH, '(//*[@class="ui-range__dot"])[2]')
        actions.click_and_hold(el_2).move_by_offset(xoffset=-60, yoffset=0).perform()
        driver.find_element(By.XPATH, "//span[contains(text(), 'Android')]").click()
        WebDriverWait(set_up_browser, 3).until(EC.presence_of_element_located((
            By.XPATH, "//*[@class = 'courses-block courses-section__block']"
        )))
        profession1 = driver.find_element(By.XPATH, "(//*[@class = 'ui-product-card-main__title t t--2'])[1]").text
        profession2 = driver.find_element(By.XPATH, "(//*[@class = 'ui-product-card-main__title t t--2'])[2]").text
        with allure.step('Проверка найденных профессий'):
            assert profession1 == "Android-разработчик"
            assert profession2 == "Мобильный разработчик"

    def test_case5(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        graph = driver.find_element(By.XPATH, '//*[@height="100"]')
        action = ActionChains(driver)
        action.move_to_element(graph).perform()
        WebDriverWait(set_up_browser, 3).until(EC.presence_of_element_located((
            By.XPATH, "(//*[contains(text(), 'commits')])[2]"
        )))
        tooltip = driver.find_element(By.CLASS_NAME, "svg-tip").text
        with allure.step('Проверка tooltip'):
            assert tooltip == "381 commits the week of Sep 3"










