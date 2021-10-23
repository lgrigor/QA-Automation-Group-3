import time

import pytest
from Regression.Pages.HomePage import HomePage


class Test_HomePage(HomePage):
  
    def test_dragging_slides(self, setUp):

        self.browser = setUp
        self.browser.get(HomePage.URL)

        time.sleep(3)
        self.drag(HomePage.SLIDE_1)
        assert self.check_visibility_of_element(HomePage.SLIDE_2), 'Second slide is not visible'

        time.sleep(3)
        self.drag(HomePage.SLIDE_2)
        assert self.check_visibility_of_element(HomePage.SLIDE_3), 'Third slide is not visible!'

        self.close_browser()
