from pages.login_page import LoginPage
from testData.user_accounts import invalid_account
from .test_base import TestBase


class InvalidLoginTest(TestBase):

    def test_login_with_invalid_credentials(self):
        login_page = LoginPage(self.driver).navigate()

        login_page.login_with_credentials(invalid_account["email"],
                                          invalid_account["password"]).assert_login_error_msg_is_displayed()
