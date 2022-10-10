from nop_excel_lib import read_locators
from nopcommerce_wrapper import Wrapper

class LoginPage(Wrapper):
    def __init__(self, driver):
        super().__init__(driver)

    locators = read_locators("login")

    def enter_email(self, email):
        element = LoginPage.locators['email']
        self.enter_text(element, value=email)
    
    def enter_password(self, password):
        element = LoginPage.locators['password']
        self.enter_text(element, value=password)

    def click_login(self):
        element = LoginPage.locators['login']
        self.click_element(element)