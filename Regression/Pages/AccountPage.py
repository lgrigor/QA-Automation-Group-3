from Regression.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AccountPage(BasePage):

    #Constants
    URL = 'http://practice.automationtesting.in/my-account/'
    TITLE = 'My Account – Automation Practice Site'

    #Locators
    REG_EMAIL = (By.ID, 'reg_email')
    REG_PASSWORD = (By.ID, 'reg_password')
    REG_BUTTON = (By.NAME, 'register')

    RANDOM = (By.XPATH, '//div[@id="customer_login"]')
    CONTENT = (By.XPATH, '//div[@class="woocommerce"]/div[@class="woocommerce-MyAccount-content"]')
    
    PASS_STRENGTH = (By.XPATH, '//p[contains(@class,"woocommerce-FormRow")]/div[contains(@class, "woocommerce-password-strength")]')
    ERROR_MESSAGE = (By.XPATH, '//ul[@class="woocommerce-error"]/li/strong')