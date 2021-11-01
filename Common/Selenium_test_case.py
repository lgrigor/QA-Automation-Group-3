import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


EMAIL = 'ghjgj'
PASSWORD = 'd1$^%S$dw123$dSDADSsa4_^$d+'

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--log-level=3')
#chrome_options.add_argument('--headless')

browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
browser.get('http://practice.automationtesting.in/')
browser.set_page_load_timeout(15)
browser.implicitly_wait(15)


#browser.find_element(By.ID, 'menu-item-40').click()

#browser.find_element(By.XPATH, '//div[@id="content"]/nav/a[text()= "Home"]').click()

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

count = browser.find_elements(By.XPATH, '//a[@class="woocommerce-LoopProduct-link"]')
assert len(count) == 3, 'Somethimg went wrong!'



browser.find_element(By.XPATH, '//div[@class="woocommerce"]').click()

browser.find_element(By.XPATH, '//form[@class="cart"]/button[@type="submit"]').click()



amount = browser.find_element(By.XPATH, '//div[@class="summary entry-summary"]//p/span[@class="woocommerce-Price-amount amount"]')


item = browser.find_element(By.XPATH, '//span[@class="cartcontents"]')

top_amount = browser.find_element(By.XPATH, '//span[@class="amount"]')
assert item.text == "1 Item", 'Somethimg went wrong again!'
assert top_amount.text == amount.text, 'Amount text is wrong!'

item = browser.find_element(By.XPATH, '//span[@class="cartcontents"]').click()


total = float(browser.find_element(By.XPATH, '//td[@data-title="Total"]/strong/span').text[1:])
subtotal = float(browser.find_element(By.XPATH, '//td[@data-title="Subtotal"]/span').text[1:])

assert subtotal < total, f'subtotal is greater or equal to total: total - {total}, subtotal - {subtotal}'

# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
browser.find_element(By.XPATH, '//div[@class="wc-proceed-to-checkout"]/a').click()

browser.find_element(By.ID, 'billing_first_name').send_keys("Susanna")

time.sleep(5)

browser.quit()
