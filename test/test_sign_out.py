from pages.account_home_page import AccountHomePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from testData.user_accounts import valid_account
from .test_base import TestBase


class SignOutTest(TestBase):

    def test_signing_out_of_account_is_successful(self):
        account_home_page = AccountHomePage(self.driver)
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver).navigate()

        login_page.login_with_credentials(valid_account["email"], valid_account["password"])

        account_home_page.log_out_of_account()

        # user should be redirected to home page after log out
        home_page.assert_user_is_on_hudl_home_page()
