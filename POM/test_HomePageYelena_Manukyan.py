import time
import pytest
#from config import TestData
from HomePage import HomePage


class Test_HomePage(HomePage):
    def test_enter(self, setUp):
        self.browser = setUp
        self.browser.get(HomePage.URL)
        time.sleep(0.5)
        
        self.click(HomePage.Slide1)
        time.sleep(0.5)
        self.click(HomePage.Slide2)
        time.sleep(0.5)
        self.click(HomePage.Shop_Btn)
        time.sleep(0.5)
        self.click(HomePage.My_Account_Btn)
        time.sleep(0.5)
        self.click(HomePage.Test_Cases_Btn)
        time.sleep(0.5)
        self.click(HomePage.Items_Btn)
        time.sleep(0.5)
        self.browser.get(HomePage.URL)
        time.sleep(0.5)
        self.click(HomePage.Selenium_Ruby)
        time.sleep(0.5)
        self.browser.get(HomePage.URL)
        time.sleep(0.5)
        self.click(HomePage.Thinking_HTML)
        time.sleep(0.5)
        self.browser.get(HomePage.URL)
        time.sleep(0.5)
        self.click(HomePage.Mastering_JavaScript)
        time.sleep(0.5)
        self.browser.get(HomePage.URL)
        time.sleep(0.5)
        self.close_browser()
        
        

