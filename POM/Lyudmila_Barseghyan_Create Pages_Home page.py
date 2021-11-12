from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains





class BasePage():

    def click(self, by_locator):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def check_visibility_of_element(self, by_locator):
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            self.close_browser()
            return False
            
    def close_browser(self):
        self.browser.quit()



class Locators(BasePage):

    #Constants
    URL = 'http://practice.automationtesting.in'

    #Locators

    SHOP = (By.XPATH, "//a[contains(text(),'Shop')]")
    MY_ACCOUNT = (By.XPATH, "//a[contains(text(),'My Account')]")
    TEST_CASES = (By.XPATH, "//a[contains(text(),'Test Cases')]")
    AT_SITE = (By.XPATH, "//a[contains(text(),'AT Site')]")
    DEMO_SITE = (By.XPATH, "//a[contains(text(),'Demo Site')]")
    CART = (By.XPATH, "//a[@title='View your shopping cart']")
    EMAIL = (By.XPATH, "//input[@name='EMAIL']")
    SUBSCRIBE =  (By.XPATH, "//input[@type='submit']")
    HOME_PAGE = (By.XPATH, "//a[@title='Automation Practice Site']")
    ADD_TO_CARD_1 = (By.XPATH, "//a[@data-product_id='160']")
    ADD_TO_CARD_2 = (By.XPATH, "//a[@data-product_id='163']")
    ADD_TO_CARD_3 = (By.XPATH, "//a[@data-product_id='165']")
    SLIDER = (By.XPATH, '//div[@id="n2-ss-6"]')



class TestPage(Locators):

    def test_page(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--log-level=3')
        self.chrome_options.add_argument('--start-maximized')
        self.browser = webdriver.Chrome('chromedriver', options=self.chrome_options)
        self.browser.get(Locators.URL)

        time.sleep(1.5)
        self.click(Locators.ADD_TO_CARD_1)

        time.sleep(1.5)
        self.click(Locators.ADD_TO_CARD_2)

        time.sleep(1.5)
        self.click(Locators.ADD_TO_CARD_3)
        
        time.sleep(0.5)
        self.click(Locators.SHOP)

        time.sleep(0.5)
        self.click(Locators.MY_ACCOUNT)

        time.sleep(0.5)
        self.click(Locators.TEST_CASES)

        time.sleep(0.5)
        self.click(Locators.AT_SITE)
        self.browser.back()

        time.sleep(0.5)
        self.click(Locators.DEMO_SITE)
        self.browser.back()

        time.sleep(0.5)
        self.click(Locators.CART)

        time.sleep(0.5)
        self.click(Locators.HOME_PAGE)

        time.sleep(0.5)
        self.send_keys(Locators.EMAIL, 'lyuka-@gmail.com')
        self.click(Locators.SUBSCRIBE)


        time.sleep(0.5)
        slider = self.browser.find_element_by_xpath('//div[@id="n2-ss-6"]')
        ActionChains(self.browser).drag_and_drop_by_offset(slider, -50, 0).perform()
        ActionChains(self.browser).drag_and_drop_by_offset(slider, -50, 0).perform()
        ActionChains(self.browser).drag_and_drop_by_offset(slider, -50, 0).perform()
        time.sleep(1)
    
        self.close_browser()
