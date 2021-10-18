#1) Open the browser
#2) Enter the URL “”
#3) Click on My Account Menu
#4) Enter registered Email Address in Email-Address textbox
#5) Enter your own password in password textbox
#6) Click on Register button
#7) User will be registered successfully and will be navigated to the Home page

import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

EMAIL = 'd2s1q5dsdqwdwqdqdqadsad6w@dksadas.com'
PASSWORD = 'd1$^%S$dw123$dSDADSsa4_^$d+'

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--log-level=3')

browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
browser.get('http://practice.automationtesting.in/')
browser.set_page_load_timeout(15)
browser.implicitly_wait(5)

browser.find_element(By.ID, 'menu-item-50').click()
browser.find_element_by_id('reg_email').send_keys(EMAIL)
browser.find_element_by_id('reg_password').send_keys(PASSWORD)

time.sleep(1)
browser.find_element(By.XPATH, '//div[@id="customer_login"]').click()

try:
    browser.find_element(By.XPATH, '//div[@class="woocommerce-password-strength strong"]')
except NoSuchElementException:
    raise Exception('password-strength')

browser.find_element_by_name('register').click()

try:
    browser.find_element(By.XPATH, '//div[@class="woocommerce"]/div[@class="woocommerce-MyAccount-content"]')
except NoSuchElementException:
    assert False, 'message'

browser.find_element(By.XPATH, '//div[@class="woocommerce-MyAccount-content"]/p/a').click()

try:
    browser.find_element(By.XPATH, '//div[@id="customer_login"]')
except NoSuchElementException:
    assert False, 'message'

browser.quit()