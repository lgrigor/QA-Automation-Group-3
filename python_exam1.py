from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

PATH = r"C:\Program Files (x86)\chromedriver_94.exe"
browser = webdriver.Chrome(PATH)
browser.maximize_window()

#1) Open the browser
#2) Enter the URL “http://practice.automationtesting.in/”
browser.get("http://practice.automationtesting.in/")
browser.implicitly_wait(15)

#3) Click on Shop Menu
browser.find_element(By.ID, "menu-item-40").click()

#4) Click on Home menu button
browser.find_element(By.XPATH, "//div[@id='content']//a[@href='http://practice.automationtesting.in']").click()

#5) Test whether the Home page has Three Arrivals only
#6) The Home page must contains only three Arrivals
arrivals = browser.find_elements(By.XPATH,  "//div[@class='tb-column-inner']/div[2]/div")
assert len(arrivals) == 3, "Items count is not 3"

#7) Click the image in the Arrivals
currentURL_before_Click_onPicture = browser.current_url
picture = browser.find_elements_by_class_name("woocommerce-LoopProduct-link")
picture[0].click()
currentURL = browser.current_url
#8) Test whether it is navigating to next page where the user can add that book into his basket
#9) Image should be clickable and shoul navigate to next page where user can add that book to his basket
assert currentURL_before_Click_onPicture != currentURL, "User did not navigate to next page"

BasketItemCount = browser.find_element(By.XPATH, "//li[@id='wpmenucartli']//span[@class='cartcontents']").text
listItemCount = str(BasketItemCount).split()
itemBeforeAddingNewItem = listItemCount[0]

#10) Click on the Add To Basket button which adds that book to your basket
browser.find_element(By.XPATH, "//div[@id='content']/div//button[@type='submit']").click()

BasketItemCountAfter = browser.find_element(By.XPATH, "//li[@id='wpmenucartli']//span[@class='cartcontents']").text
listItemCount = str(BasketItemCountAfter).split()
itemAfterAddingNewItem = listItemCount[0]

#11) User can view that Book in the Menu item with price.
assert itemBeforeAddingNewItem < itemAfterAddingNewItem, "Something went incorrect, item did not added in Basket"

#12) Click on Item link which navigates to proceed to check out page.
browser.find_element(By.ID, "wpmenucartli").click()

#13) Now user can find total and subtotal values just above the Proceed to Checkout button.
assert browser.find_element(By.CLASS_NAME, "wc-proceed-to-checkout").is_displayed(), "proceed-to-checkout is not visible"


#14) The total always > subtotal because taxes are added in the subtotal
subtotal = browser.find_element(By.XPATH, "//tr[@class='cart-subtotal']/td/span").text
x = subtotal[1:]

total = browser.find_element(By.XPATH, "//table[@class='shop_table shop_table_responsive']//strong/span").text
y = total[1:]
assert float(x) < float(y), "The total always > subtotal"


#15) Click on Proceed to Check out button which navigates to payment gateway page.
#16) User can view Billing Details,Order Details,Additional details and Payment gateway details.
browser.find_element(By.CLASS_NAME, "checkout-button").click()


#17) Fill his details in billing details form and can opt any payment in the payment gateway like Direct bank transfer,cheque,cash or paypal.
browser.find_element(By.ID, "billing_first_name").send_keys("Gevorg")
browser.find_element(By.ID, "billing_last_name").send_keys("Paloyan")
browser.find_element(By.ID, "billing_email").send_keys("gevpaloyan@gmail.com")
browser.find_element(By.ID, "billing_phone").send_keys("+37477503737")
browser.find_element(By.ID, "s2id_billing_country").click()
country = browser.find_element(By.ID, "s2id_autogen1_search")
country.send_keys("Armenia")
country.send_keys(Keys.TAB)

browser.find_element(By.ID, "billing_address_1").send_keys("Argishti1")
browser.find_element(By.ID, "billing_city").send_keys("Musaler")
browser.find_element(By.ID, "billing_state").send_keys("Arg")
browser.find_element(By.ID, "billing_postcode").send_keys("1045")
time.sleep(3)
#18) Now click on Place Order button to complete process
browser.find_element(By.XPATH, "//input[@id='place_order']").click()


#19) On clicking place-order button user completes the process where the page navigates to Order confirmation page
#with order details,bank details,customer details and billing details.
message = browser.find_element(By.XPATH, "//p[@class='woocommerce-thankyou-order-received']").text
assert message == "Thank you. Your order has been received.", "User did not completed the order process"

browser.close()


### Good Job !!!