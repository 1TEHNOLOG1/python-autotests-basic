from selenium import webdriver
from chromedriver_py import binary_path
import pytest
from logger import setup_logger

logger = setup_logger()


@pytest.fixture()
def set_up_browser():
    svc = webdriver.ChromeService(executable_path=binary_path)
    logger.info("Start")
    driver = webdriver.Chrome(service=svc)
    options = webdriver.ChromeOptions()
    options.headless = True
    driver.implicitly_wait(10)
    yield driver
    logger.info("stop")
    driver.quit()
