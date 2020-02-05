import unittest

from selenium import webdriver


# Test base class that other tests will inherit from
# Will handle setup/teardown of webdriver


class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
