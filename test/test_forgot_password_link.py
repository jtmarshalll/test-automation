from pages.login_page import LoginPage
from .test_base import TestBase


class ForgotPasswordLinkTest(TestBase):

    def test_forgot_password_link_sends_user_to_reset_password_form(self):
        login_page = LoginPage(self.driver).navigate()

        login_page.click_forgot_password_link().assert_reset_password_form_is_displayed()
