from selenium.webdriver.common.by import By

from conf import environment
from .base_page import BasePage


class HomePage(BasePage):
    TITLE = "Hudl: We Help Teams and Athletes Win"
    URL = environment.base_url + "/"

    # Home Page Locators
    LOGIN_LINK = {"by": By.CSS_SELECTOR, "using": ".nav-button a.login"}
    SIGN_UP_LINK = {"by": By.LINK_TEXT, "using": "Sign Up"}

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        return self.go_to_url(self.URL)

    def assert_user_is_on_hudl_home_page(self):
        self.wait_until_title_is(self.TITLE)
        self.wait_until_visible(self.LOGIN_LINK)
        assert self.driver.current_url == self.URL
        return self
