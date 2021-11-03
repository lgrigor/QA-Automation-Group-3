from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage ():
    def click(self,locator):
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(locator)).click()
    def send_keys(self,locator,text):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
    def close_browser(self):
        self.browser.quit()
    def find_element(self,locator):
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            self.close_browser()
            return False


    