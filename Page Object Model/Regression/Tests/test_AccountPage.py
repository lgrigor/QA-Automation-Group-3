import time

import pytest
from Regression.Config.config import TestData
from Regression.Pages.AccountPage import AccountPage


class Test_AccountPage(AccountPage):

    def test_registration_valid_login_password(self, setUp):

        self.browser = setUp
        self.browser.get(AccountPage.URL)
        
        time.sleep(0.5)
        self.send_keys(AccountPage.REG_EMAIL, TestData.VALID_EMAIL)

        time.sleep(0.5)
        self.send_keys(AccountPage.REG_PASSWORD, TestData.VALID_PASSWORD)

        time.sleep(0.5)
        self.click(AccountPage.RANDOM)
        assert self.check_visibility_of_element(AccountPage.PASS_STRENGTH), 'Missed password strength!'

        time.sleep(0.5)
        self.click(AccountPage.REG_BUTTON)
        assert self.check_visibility_of_element(AccountPage.ERROR_MESSAGE), 'Missed error message!'
    
        self.close_browser()
        
    def test_registration_random_login_password(self, setUp):
        
        self.browser = setUp
        self.browser.get(AccountPage.URL)
        
        time.sleep(0.5)
        self.send_keys(AccountPage.REG_EMAIL, TestData.RANDOM_EMAIL)

        time.sleep(0.5)
        self.send_keys(AccountPage.REG_PASSWORD, TestData.RANDOM_PASSWORD)

        time.sleep(0.5)
        self.click(AccountPage.RANDOM)
        assert self.check_visibility_of_element(AccountPage.PASS_STRENGTH), 'Missed password strength!'

        time.sleep(0.5)
        self.click(AccountPage.REG_BUTTON)
        assert self.check_visibility_of_element(AccountPage.CONTENT), 'Missed page content!'

        self.close_browser()
