from time import sleep
from wait import _waiting

class Wrapper:
    def __init__(self, driver):
        self.driver = driver

    @_waiting
    def enter_text(self,locator,*,value):
        self.driver.find_element(*locator).clear()
        sleep(3)
        self.driver.find_element(*locator).send_keys(value)

    @_waiting
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

        