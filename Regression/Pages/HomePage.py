from Regression.Pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage(BasePage):

    #Constants
    URL = 'http://practice.automationtesting.in/'
    TITLE = 'Automation Practice Site'

    #Locators
    ACTIVE_SLIDE = (By.XPATH, '//div[contains(@class, "n2-ss-slide-active")]')
    SLIDE_1 = (By.XPATH, '//div[@data-id="36"]')
    SLIDE_2 = (By.XPATH, '//div[@data-id="34"]')
    SLIDE_3 = (By.XPATH, '//div[@data-id="35"]')  

    #Methods
    def drag(self, slide):

        action = ActionChains(self.browser)
        source = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(slide))
        action.drag_and_drop_by_offset(source, -300, 0).pause(3).perform()
