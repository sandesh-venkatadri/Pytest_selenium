from time import sleep
from selenium.webdriver import Chrome
from config import Config
from pytest import fixture

@fixture(scope="function")
def setup():
    driver = Chrome(Config.driver_path)
    driver.get(Config.url)
    driver.maximize_window()
    sleep(3)
    yield driver
    sleep(5)
    driver.close()