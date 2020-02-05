from selenium.webdriver.common.by import By

from conf import environment
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_ERROR_MESSAGE = "We didn't recognize that email and/or password. Need help?"
    URL = environment.base_url + "/login"

    # Login Page Locators
    EMAIL_INPUT = {"by": By.ID, "using": "email"}
    LOGIN_BUTTON = {"by": By.ID, "using": "logIn"}
    LOGIN_ERROR = {"by": By.CLASS_NAME, "using": "login-error-container"}
    PASSWORD_INPUT = {"by": By.ID, "using": "password"}

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        return self.go_to_url(self.URL)

    def enter_email(self, email):
        self.set_value(self.EMAIL_INPUT, email)
        return self

    def enter_password(self, password):
        self.set_value(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        return self

    def login_with_credentials(self, email, password):
        self.enter_email(email).enter_password(password).click_login()
        return self

    def assert_login_error_msg_is_displayed(self):
        assert self.get_element(self.LOGIN_ERROR).text == self.LOGIN_ERROR_MESSAGE
        return self
