from selenium import webdriver
from chromedriver_py import binary_path
import pytest


@pytest.fixture()
def set_up_browser():
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    options = webdriver.ChromeOptions()
    options.headless = True
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
