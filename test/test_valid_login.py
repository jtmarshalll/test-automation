from pages.account_home_page import AccountHomePage
from pages.login_page import LoginPage
from testData.user_accounts import valid_account
from .test_base import TestBase


class LoginTest(TestBase):

    def test_login_with_valid_credentials(self):
        login_page = LoginPage(self.driver).navigate()
        account_home_page = AccountHomePage(self.driver)

        login_page.login_with_credentials(valid_account["email"], valid_account["password"])
        account_home_page.assert_user_is_on_account_home_page()
