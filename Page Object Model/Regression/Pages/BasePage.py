from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage():

    def click(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def shop_button(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, 'menu-item-40'))).click()

    def myaccount_button(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, 'menu-item-50'))).click()

    def get_item_count(self):
        ITEM_COUNT_LOCATOR = (By.XPATH, '//a[@class="wpmenucart-contents empty-wpmenucart-visible"]/span[@class="cartcontents"]')
        count = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(ITEM_COUNT_LOCATOR)).text()
        return count

    def get_total_amount(self):
        ITEM_AMOUNT_LOCATOR = (By.XPATH, '//a[@class="wpmenucart-contents empty-wpmenucart-visible"]/span[@class="amount"]')
        amount = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(ITEM_AMOUNT_LOCATOR)).text()
        return amount

    def check_visibility_of_element(self, by_locator):
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            self.close_browser()
            return False
            
    def close_browser(self):
        self.browser.quit()