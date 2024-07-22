from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestCases:
    def test_case1(self, set_up_browser):
        driver = set_up_browser
        driver.get(' https://github.com/microsoft/vscode/issues')
        driver.find_element(By.ID, 'js-issues-search').send_keys('in:title bug')
        driver.find_element(By.ID, 'js-issues-search').send_keys(Keys.ENTER)
        pass

    def test_case2(self, set_up_browser):
        driver = set_up_browser
        driver.get(' https://github.com/microsoft/vscode/issues')
        driver.find_element(By.XPATH, '//*[@title="Author"]').click()
        driver.find_element(By.ID, 'author-filter-field').send_keys('bpasero')
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, '//*[@class="SelectMenu-list select-menu-list is-showing-new-item-form"]').click()
        driver.implicitly_wait(5)
        time.sleep(5)


    def test_case3(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/search/advanced')
        driver.find_element(By.ID, 'search_language').click()
        driver.find_element(By.XPATH, '//option[@value="Python"]').click()
        driver.find_element(By.ID, 'search_stars').send_keys('>20000')
        driver.find_element(By.ID, "search_filename").send_keys('environment.yml')
        driver.find_element(By.CSS_SELECTOR, '.btn.flex-auto').click()
        time.sleep(6)
        pass

    def test_case4(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        driver.get('https://skillbox.ru/code/')
        driver.find_element(By.XPATH, '//*[@value="profession"]').click()
        el_1 = driver.find_element(By.XPATH, '(//*[@class="ui-range__dot"])[1]')
        actions = ActionChains(driver)
        actions.click_and_hold(el_1).move_by_offset(xoffset=50, yoffset=0).perform()
        el_2 = driver.find_element(By.XPATH, '(//*[@class="ui-range__dot"])[2]')
        actions.click_and_hold(el_2).move_by_offset(xoffset=-60, yoffset=0).perform()
        time.sleep(5)
        pass

    def test_case5(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        driver.implicitly_wait(4)
        driver.find_element(By.XPATH, '//*[@height="100"]')
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH,'//*[@height="100"]' )).perform()
        time.sleep(10)
