from admin_loginpage_pom import LoginPage
from config import Config
from nopcommerce_wrapper import Wrapper


def test_login(setup):
    lp = LoginPage(setup)
    lp.enter_email(Config.email)
    lp.enter_password(Config.password)
    lp.click_login()
