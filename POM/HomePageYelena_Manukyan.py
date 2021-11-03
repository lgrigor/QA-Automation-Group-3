from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from BasePage import BasePage


class HomePage(BasePage):
    URL = 'http://practice.automationtesting.in/'

    Shop_Btn = (By.ID, 'menu-item-40')  
    My_Account_Btn = (By.ID, 'menu-item-50')
    Test_Cases_Btn = (By.ID, 'menu-item-224')
    Items_Btn = (By.CSS_SELECTOR, 'span.cartcontents')
    Selenium_Ruby = (By.XPATH, "//a[@class='woocommerce-LoopProduct-link']/img[@width='300']")
    Thinking_HTML = (By.XPATH, "//a[@class='woocommerce-LoopProduct-link']/img[@alt='Thinking in HTML']")
    Mastering_JavaScript = (By.XPATH, "//a[@class='woocommerce-LoopProduct-link']/img[@alt='Mastering JavaScript']")
    Slide1 = (By.XPATH, "//img[@class='n2-ow']")
    Slide2 = (By.XPATH, "//img[@class='n2-ow']")
