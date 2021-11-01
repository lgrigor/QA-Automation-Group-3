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


EMAIL = 'ghjgj'
PASSWORD = 'd1$^%S$dw123$dSDADSsa4_^$d+'

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--log-level=3')

browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
browser.get('http://practice.automationtesting.in/')
browser.set_page_load_timeout(10)
browser.implicitly_wait(10)


browser.find_element(By.ID, 'menu-item-40').click()

browser.find_element(By.XPATH, '//div[@id="content"]/nav/a[text()= "Home"]').click()

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


subtotal = browser.find_element(By.XPATH, '//tr[@class="cart-subtotal"]/td[@data-title="Subtotal"]/span[@class="woocommerce-Price-amount amount"]')
total = browser.find_elements(By.XPATH, '//span[@class="woocommerce-Price-amount amount"]')
print(total)

exit(0)
assert subtotal.text < total.text, 'It is wrong!'

# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
browser.find_element(By.LINK_TEXT, '//a[text()= "Proceed to Checkout"]').click()

# browser.find_element(By.ID, 'billing_first_name').send_keys("Susanna")



browser.quit()