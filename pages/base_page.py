from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conf.environment import webdriver_timeout


# Base page object class other page object will inherit from


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_title_is(self, title):
        WebDriverWait(self.driver, webdriver_timeout).until(EC.title_is(title))
        return self

    def wait_until_clickable(self, locator):
        return WebDriverWait(self.driver, webdriver_timeout).until(
            EC.element_to_be_clickable((locator["by"], locator["using"])))

    def wait_until_visible(self, locator):
        return WebDriverWait(self.driver, webdriver_timeout).until(
            EC.visibility_of_element_located((locator["by"], locator["using"])))

    def wait_until_element_contains_text(self, locator, text):
        WebDriverWait(self.driver, webdriver_timeout).until(
            EC.text_to_be_present_in_element((locator["by"], locator["using"]), text))
        return self

    def go_to_url(self, url):
        self.driver.get(url)
        return self

    def get_element(self, locator):
        return self.wait_until_visible(locator)

    def click(self, locator):
        self.wait_until_clickable(locator).click()

    def set_value(self, locator, value):
        self.get_element(locator).send_keys(value)

    def hover_element(self, locator):
        element = self.get_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        return self
