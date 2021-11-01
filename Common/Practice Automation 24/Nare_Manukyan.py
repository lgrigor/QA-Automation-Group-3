import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

# Open the browser
driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument('--log-level=3')

# Enter the URL “http://practice.automationtesting.in/”
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.find_element(By.XPATH, '//div[@id="site-logo"]').click()

# Click on Shop Menu
driver.find_element(By.ID, 'menu-item-40').click()
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'content')))

# Click on Home menu button
driver.find_element(By.XPATH, '//nav[@class="woocommerce-breadcrumb"]/a').click()
driver.execute_script("window.scrollBy(0,800)")

# Test whether the Home page has Three Arrivals only and check the count
product_count = len(driver.find_elements(By.XPATH, '//div[@class="woocommerce"]'))

assert product_count == 3, "Product count isn't 3"

# Click the image in the Arrivals and test whether it is navigating to next page.
driver.find_element(By.XPATH, "//div[@id='text-22-sub_row_1-0-2-2-0']").click()

assert "Mastering JavaScript – Automation Practice Site" in driver.title

# Click on the Add To Basket button which adds that book to your basket
basket_amount = driver.find_element(By.XPATH, '//span[@class="amount"]').text[1:]
driver.find_element(By.XPATH, '//form[@class="cart"]/button').click()

# User can view that Book in the Menu item with price
book_price = driver.find_element(By.XPATH, '//p[@class="price"]').text[1:]
total = driver.find_element(By.XPATH, '//span[@class="amount"]').text[1:]
basket_total_amount = (format((float(basket_amount) + float(book_price)), '.2f'))

assert basket_total_amount == total, 'Book Price and Basket '

# Click on Item link which navigates to proceed to check out page.
time.sleep(1)
driver.find_element(By.XPATH, '//i[@class="wpmenucart-icon-shopping-cart-0"]').click()
driver.execute_script("window.scrollBy(0,200)")

# Total always > subtotal because taxes are added in the subtotal
subtotal = driver.find_element(By.XPATH, '//td[@data-title="Subtotal"]').text[1:]
roaming_tax = driver.find_element(By.XPATH, '//td[@data-title="Roaming Tax"]').text[1:]
actual_total = str(format((float(subtotal) + float(roaming_tax)), '.2f'))
expected_total = driver.find_element(By.XPATH, '//tr[@class="order-total"]/td').text[1:]

assert actual_total == expected_total, "Actual and Expected totals are different"
assert float(subtotal) < float(expected_total), "total isn't greater than subtotal"

# Now click on Proceed to Check out button which navigates to payment gateway page.
driver.find_element(By.XPATH, '//div[@class="wc-proceed-to-checkout"]/a').click()

assert "Checkout – Automation Practice Site" in driver.title

# User can view Billing Details,Order Details,Additional details and Payment gateway details.
try:
    driver.find_element(By.XPATH, '//div[@class="woocommerce-billing-fields"]')
    driver.find_element(By.XPATH, '//div[@class="woocommerce-shipping-fields"]')

    driver.find_element(By.ID, 'order_review')
    driver.execute_script( "window.scrollBy(0,1000)")
    time.sleep(1)
    payment = driver.find_element(By.ID, 'payment')

except NoSuchElementException:
    print("No element found")

""" User can fill his details in billing details form and
    can opt any payment in the payment gateway like
    Direct bank transfer,cheque,cash or paypal."""

driver.find_element(By.NAME, 'billing_first_name').send_keys('Name')
driver.find_element(By.NAME, 'billing_last_name').send_keys('Surname')
driver.find_element(By.ID, 'order_comments').send_keys('Order details')
driver.find_element(By.NAME, 'billing_company').send_keys('Company')
num = "".join(list(map(str, random.sample(range(458, 647), 1))))
driver.find_element(By.NAME, 'billing_email').send_keys('email' + num + '@email.com')
driver.find_element(By.NAME, 'billing_phone').send_keys('00786775787')
driver.find_element(By.ID, 's2id_billing_country').click()
driver.find_element(By.ID, 's2id_autogen1_search').send_keys('Argentina')
driver.find_element(By.XPATH, '//span[text()="Argentina"]').click()
driver.find_element(By.NAME, 'billing_address_1').send_keys('Adress 1')
driver.find_element(By.NAME, 'billing_address_2').send_keys('Adress 2')
driver.find_element(By.NAME, 'billing_city').send_keys('City')
driver.find_element(By.ID, 's2id_billing_state').click()
driver.find_element(By.XPATH, '//div[text()="Buenos Aires"]').click()
driver.find_element(By.ID, 'billing_postcode').send_keys('0001')
driver.find_element(By.ID, 'createaccount').click()
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'account_password')))
password.send_keys('password123!ASD')
time.sleep(2)
driver.find_element(By.ID, 'payment_method_cod').click()

# Click on Place Order button to complete process
driver.find_element(By.ID, 'place_order').click()

"""On clicking place-order button user completes the process where
   the page navigates to Order confirmation page with order details,
   bank details,customer details and billing details.
   I mentioned only order details because other info isn't visible in the website"""

order_approved = (By.XPATH, '//p[text()="Thank you. Your order has been received."]')
try:
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(order_approved, 'Thank you. Your order has been received.'))
    driver.find_element(By.XPATH, '//table[@class="shop_table order_details"]')
    driver.close()
except:
    print("Order isn't approved")
