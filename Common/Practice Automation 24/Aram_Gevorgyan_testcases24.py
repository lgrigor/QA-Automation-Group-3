from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--log-level=3')

#1
browser = webdriver.Chrome(r'C:\Users\Aram\Drivers\chromedriver.exe')
#2
browser.get("http://practice.automationtesting.in/")
browser.set_page_load_timeout(10)
browser.implicitly_wait(5)
#3
time.sleep(2)
browser.find_element(By.ID, 'menu-item-40').click()
#4
time.sleep(2)
browser.find_element(By.XPATH, "//div/nav[@class = 'woocommerce-breadcrumb']/a").click()
#5, 6, 7, 8
time.sleep(2)
elements = browser.find_elements(By.XPATH, "//a[@class = 'woocommerce-LoopProduct-link']")
#print(len(elements))
assert len(elements) == 3, f'The number of products is {len(elements)}, must be 3!'
elements[0].click()
#9
time.sleep(2)
assert browser.current_url == "http://practice.automationtesting.in/product/selenium-ruby/", f"the page is not located"
#10
time.sleep(2)
browser.find_element(By.XPATH, "//form[@class = 'cart']/button[@type = 'submit']").click()
#11
time.sleep(2)
count = browser.find_element(By.XPATH, "//*[@id='wpmenucartli']/a/span[1]").text
#print(count)
assert count == '1 Item', f'The count of products must be 1!'

amount = browser.find_element(By.XPATH, "//*[@id='wpmenucartli']/a/span[2]").text
#print(amount)
assert amount == '₹500.00', f'The amount of products must be 500.00!'
#12, 13
time.sleep(2)
browser.find_element(By.ID, "wpmenucartli").click()
#14
time.sleep(2)
subtotal = browser.find_element(By.XPATH, "//tr[@class='cart-subtotal']/td/span").text
Subtotal = subtotal[1:]
total = browser.find_element(By.XPATH, "//table[@class='shop_table shop_table_responsive']//strong/span").text
Total = total[1:]
assert float(Subtotal) < float(Total), "The Subtotal is always < Total"
#15
time.sleep(2)
browser.find_element(By.CLASS_NAME, "checkout-button").click()
#16, 17
time.sleep(2)
browser.find_element(By.ID, "billing_first_name").send_keys("AAAAA")
time.sleep(1)
browser.find_element(By.ID, "billing_last_name").send_keys("GGGGG")
time.sleep(1)
browser.find_element(By.ID, "billing_email").send_keys("AAAGGGAAA@gmail.com")
time.sleep(1)
browser.find_element(By.ID, "billing_phone").send_keys("+123456789")
time.sleep(1)
browser.find_element(By.ID, "s2id_billing_country").click()
country = browser.find_element(By.ID, "s2id_autogen1_search")
country.send_keys("Armenia")
country.send_keys(Keys.TAB)
time.sleep(1)
browser.find_element(By.ID, "billing_address_1").send_keys("Mars")
time.sleep(1)
browser.find_element(By.ID, "billing_city").send_keys("Crater")
#time.sleep(1)
browser.find_element(By.ID, "billing_state").send_keys("Mr")
time.sleep(1)
browser.find_element(By.ID, "billing_postcode").send_keys("000111")
#16, 17
browser.find_element(By.ID, "payment_method_cod").click()
#18
time.sleep(2)
browser.find_element(By.XPATH, "//input[@id='place_order']").click()
#19
information = browser.find_element(By.XPATH, "//p[@class='woocommerce-thankyou-order-received']").text
assert information == "Thank you. Your order has been received.", "User didn't completed the order process correct"

time.sleep(4)
browser.quit()