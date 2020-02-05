from selenium.webdriver.common.by import By
from .base_page import BasePage
from conf import environment


class AccountHomePage(BasePage):
    URL = environment.base_url + "/home"

    # Account Home Page locators
    HOME_LINK = {"by": By.LINK_TEXT, "using": "Home"}
    LOG_OUT_LINK = {"by": By.LINK_TEXT, "using": "Log Out"}
    USER_MENU = {"by": By.CLASS_NAME, "using": "hui-globalusermenu"}

    def __init__(self, driver):
        self.driver = driver

    def assert_user_is_on_account_home_page(self):
        self.wait_until_visible(self.USER_MENU)
        assert self.driver.current_url == self.URL
        return self

    def log_out_of_account(self):
        self.hover_element(self.USER_MENU).click(self.LOG_OUT_LINK)
        return self
