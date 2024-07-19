from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
import pytest


@pytest.fixture()
def set_up_browser():
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    options = webdriver.ChromeOptions()
    options.headless = True
    yield driver
    driver.quit()